
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.common_name} ({self.id})' 
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
    def watered(self):
        today = datetime.today()
        week_ago = today - timedelta(days=7)
        return self.watering_set.filter(date__gte=week_ago).count() >= 2     
       
class Watering(models.Model):
    date = models.DateField('Watering Date')

    plant = models.ForeignKey(
        Plant,  
        on_delete=models.CASCADE
    )

    def __str__ (self):
        return f"Watered on {self.date}"

class Photo(models.Model):
  url = models.CharField(max_length=200)
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __self__(self):
    return f"Photo for plant_id: {self.plant_id} @{self.url}" 

   
