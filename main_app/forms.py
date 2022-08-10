from django.forms import ModelForm
from .models import Watering, Pot

class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['date']

class PotForm(ModelForm):
    class Meta:
        model = Pot
        fields = '__all__'