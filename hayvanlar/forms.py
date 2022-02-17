
from .models import  HayvanSahibi,Hayvan
from django.forms import ModelForm





class SahipForm(ModelForm):
   class Meta:
        model = HayvanSahibi
        fields = ['name', 'surname', 'email', 'phone','address']

class HayvanForm(ModelForm):
   class Meta:
        model = Hayvan
        fields = ['type', 'genus', 'name', 'age', 'owner', 'description']