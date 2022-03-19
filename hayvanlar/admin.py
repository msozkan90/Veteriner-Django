from django.contrib import admin

# Register your models herea
from .models import *

admin.site.register(Animals)
admin.site.register(AnimalOwners)