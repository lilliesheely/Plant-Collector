from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Pot
from .forms import WateringForm, PotForm
# from datetime import datetime
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

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

class PlantCreate(CreateView):
    model = Plant
    fields = ['common_name', 'latin_name', 'location', 'light', 'water', 'maintenance_level']

class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'

class PlantDelete(DeleteView): 
    model = Plant
    success_url = '/plants/'    

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

def assoc_pot(request, plant_id, pot_id):
    plant = Plant.objects.get(id=plant_id)
    plant.pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)

def unassoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)


# def watered_this_week(request):
#   today = datetime.now()
#   num_watering_this_week = Watering.objects.filter(date__year=today.year, date__month=today.month, date__week=today.week).count()
  # respond with a render?    

class PotList(ListView): 
    model = Pot

class PotCreate(CreateView):
    model = Pot
    fields = ['name', 'size', 'color', 'description']

class PotDetail(DetailView): 
    model = Pot

class PotUpdate(UpdateView): 
    model= Pot
    fields = '__all__'

class PotDelete(DeleteView):
    model = Pot
    success_url = '/pots/'


