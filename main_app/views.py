import os
import uuid 
import boto3

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Plant, Pot, Photo
from .forms import WateringForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

@login_required
def plants_index(request):
     plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    id_list = plant.pots.all().values_list('id')
    pots_plant_doesnt_have = Pot.objects.exclude(id__in=id_list)
    watering_form = WateringForm()
    return render(
        request, 
        'plants/detail.html', 
        { 
            'plant': plant, 
            'watering_form': watering_form, 
            'pots': pots_plant_doesnt_have
        }
    )

class PlantCreate(CreateView, LoginRequiredMixin):
    model = Plant
    fields = ['common_name', 'latin_name', 'location', 'light', 'water', 'maintenance_level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(UpdateView, LoginRequiredMixin):
    model = Plant
    fields = '__all__'

class PlantDelete(DeleteView, LoginRequiredMixin): 
    model = Plant
    success_url = '/plants/'    

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

@login_required
def assoc_pot(request, plant_id, pot_id):
    plant = Plant.objects.get(id=plant_id)
    plant.pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)

@login_required
def unassoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)

@login_required
def add_photo(request, plant_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, plant_id=plant_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', plant_id=plant_id)


class PotList(ListView, LoginRequiredMixin): 
    model = Pot


class PotCreate(CreateView, LoginRequiredMixin):
    model = Pot
    fields = ['name', 'size', 'color', 'description']


class PotDetail(DetailView, LoginRequiredMixin): 
    model = Pot


class PotUpdate(UpdateView, LoginRequiredMixin): 
    model= Pot
    fields = '__all__'


class PotDelete(DeleteView, LoginRequiredMixin):
    model = Pot
    success_url = '/pots/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
