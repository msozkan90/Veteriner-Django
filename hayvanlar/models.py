
from django.db import models
from django.urls import reverse


class AnimalOwners(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    address = models.TextField(max_length=40)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    @property
    def get_animals(self):
        animals = self.animals_set.all()
        return animals 
    def get_absolute_url(self):
        return reverse("hayvanlar:owner_detail", args=[str(self.id)])

class Animals(models.Model):
    type = models.CharField(max_length=15)
    genus = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    owner=models.ForeignKey(AnimalOwners, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hayvanlar:animal_detail", args=[str(self.id)])

