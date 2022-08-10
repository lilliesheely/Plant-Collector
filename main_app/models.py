from secrets import choice
from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.

class Pot(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pots_detail', kwargs={'pk': self.id})

class Plant(models.Model): 
    common_name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    light = models.CharField(max_length=50)
    water = models.CharField(max_length=200)
    maintenance_level = models.IntegerField()
    pots = models.ManyToManyField(Pot)

    def __str__(self):
        return f'{self.common_name} ({self.id})' 
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
     
class Watering(models.Model):
    date = models.DateField('Watering Date')

    plant = models.ForeignKey(
        Plant, 
        on_delete=models.CASCADE
    )

    def __str__ (self):
        return f"Watered on {self.date}"

