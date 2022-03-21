from distutils.command.clean import clean
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']
        # def clean(self):
        #     cleaned_data= super().clean()
        #     password1= cleaned_data.get('password1')
        #     password2= cleaned_data.get('password2')
        #     if password2 != password1:
        #         raise ValidationError("Passwords did not match")