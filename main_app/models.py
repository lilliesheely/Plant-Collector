from inspect import walktree
from xml.parsers.expat import model
from django.db import models


# Create your models here.
class Plant(models.Model): 
    laymen_name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    light = models.CharField(max_length=50)
    water = models.CharField(max_length=200)
    maintenance_level = models.IntegerField()

 