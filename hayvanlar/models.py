
from django.db import models


# Create your models here.

class HayvanSahibi(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    @property
    def get_animals(self):
        hayvan = self.hayvan_set.all()
        return hayvan 


class Hayvan(models.Model):
    type = models.CharField(max_length=200)
    genus = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    owner=models.ForeignKey(HayvanSahibi, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.name



