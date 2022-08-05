from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class Plant: 
    def __init__(self, laymen_name, latin_name, location, light, water, maintenance_level):
        self.laymen_name = laymen_name
        self.latin_name = latin_name
        self.location = location
        self.light = light
        self.water = water
        self.maintenance_level = maintenance_level

plants = [
    Plant('Guiana Chestnut(Money Tree)', 'Pachira aquatica', 'indoor', 'indirect light', '1-2 per week', 1 ),
    Plant('Peace Lily', 'Pachira aquatica', 'indoor', 'bright, indirect', 'Whenever top inch of soil is dry', 2 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 ),
    Plant('Prickly Pear', 'Opuntia', 'outdoor', 'direct light', '2-4 weeks (2/month in summer, 1/month rest of year', 1 )
]

def home(request):
    return HttpResponse('<h1>Hello Plant Collector!</h1>')

def about(request): 
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {
        'plants': plants
    })