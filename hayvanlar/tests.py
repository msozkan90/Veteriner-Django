from django.test import TestCase
from hayvanlar.models import Animals,AnimalOwners

class AnimalTestCase(TestCase):
    def setUp(self):
        AnimalOwners.objects.create(name="Michael", surname="Scott",address="Scranton",email="michael@gmail.com",phone="05455555555")
        Animals.objects.create(type="Cat", genus="Savannah",name="Sprinkels", age="2",owner="Michael", description="roar")


    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        owner = AnimalOwners.objects.get(name="Michael")
        animal = Animals.objects.get(name="Cat")
        self.assertEqual(owner.name(), "Owner's name Michael")
        self.assertEqual(animal.name(), "Animal's name")