
from .models import  Animals,AnimalOwners
from django.forms import ModelForm
from django import forms




class OwnersForm(ModelForm):
   class Meta:
        model = AnimalOwners
        fields = ['name', 'surname', 'email', 'phone','address']

class AnimalsForm(ModelForm):
   class Meta:
        model = Animals
        fields = ['type', 'genus', 'name', 'age', 'owner', 'description']