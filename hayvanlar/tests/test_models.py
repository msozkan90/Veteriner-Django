
from django.test import TestCase
from hayvanlar.models import AnimalOwners, Animals
from django.urls import reverse
from django.contrib.auth.models import User
USERNAME_1="example"
PASSWORD_1="example12345"
USERNAME_SUPER="examplesuper"
PASSWORD_SUPER="examplesuper12345"

class ModelTest(TestCase):
    def setUp(self):
        owner= AnimalOwners.objects.create(name="Example",surname="Example",address="Example",email="example@example.com",phone="05555555555")
        animal = Animals.objects.create(type="Example",genus="Example",name="Example",age="2",owner=owner,description="Example")

    def test_add_data_test(self):
        owner=AnimalOwners.objects.get(name="Example")
        animal=Animals.objects.get(name="Example")
        self.assertEqual(owner.name,"Example")
        self.assertEqual(animal.name,"Example")

    def test_get_absolute_url(self):
        animals = Animals.objects.get(id=1)
        owners = AnimalOwners.objects.get(id=1)
        self.assertEqual(animals.get_absolute_url(), "/animal/detail/1/")
        self.assertEqual(owners.get_absolute_url(), "/owner/detail/1/")

    def test_update_data_test(self):
        animals = Animals.objects.get(id="1")
        animals.name="example_updated"
        animals.save()
        self.assertEqual(animals.name,"example_updated")
        owners=AnimalOwners.objects.get(id="1")
        owners.name="example_updated"
        owners.save()
        self.assertEqual(owners.name,"example_updated")

    def test_delete_data_test(self):
        animals = Animals.objects.get(id="1")
        animal_delete=animals.delete()
        owners=AnimalOwners.objects.get(id="1")
        owner_delete=owners.delete()
        self.assertFalse(Animals.objects.filter(id=animals.id).exists())
        self.assertFalse(AnimalOwners.objects.filter(id=owners.id).exists())

class BaseTest(TestCase):
    def setUp(self):
        self.animal_url=reverse('hayvanlar:animals')
        self.owner_url=reverse('hayvanlar:animalowners')
        self.animal={
            'type':'type',
            'genus':'genus',
            'name':'animal',
            'age':'1',
            'owner':'',
            'description':'animal',
        }
        self.animal_type_error={
            'type':'typednejnddddddddde',
        }
        self.animal_genus_error={
            'genus':'genusssssssssssssss',
        }  
        self.animal_name_error={
            'name':'animallllllllllllllllll',
        }   
        self.animal_description_error={
            'description':'animalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimalanimal',
        }   
        self.animal_owner={
            'name':'owner',
            'surname':'owner',
            'address':'address',
            'email':'example@gmail.com',
            'phone':'05555555555'
        }
        self.animal_owner_name_error={
            'name':'ownerownerownerownerowner',
        }
        self.animal_owner_surname_error={
            'surname':'ownerownerownerownerowner',
        }
        self.animal_owner_address_error={
            'address':'addressaddressaddressaddressaddressaddressaddressaddressaddressaddress',
        }
        self.animal_owner_email_error={
            'email':'exampleexampleexampleexampleexampleexampleexamplegmail.com',
        }
        self.animal_owner_phone_error={
            'phone':'055555555555555555'
        }
        self.test_user = User.objects.create_user(USERNAME_1, 'example@gmail.com', PASSWORD_1)
        self.test_superuser = User.objects.create_superuser(USERNAME_SUPER, 'example1@gmail.com', PASSWORD_SUPER,)
        

        return super().setUp()

class AnimalFormTest(BaseTest):
    def test_animal_form_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response=self.client.post(self.animal_url,{'type':self.animal["type"],'genus':self.animal["genus"],'name':self.animal["name"],'age':self.animal["age"],'description':self.animal["description"],'owner':self.animal["owner"]},format='text/html')     
        self.assertTrue(response.url == self.animal_url)
        self.assertEqual(response.status_code,302)

    def test_animal_form_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.animal_url,{'type':self.animal["type"],'genus':self.animal["genus"],'name':self.animal["name"],'age':self.animal["age"],'description':self.animal["description"],'owner':self.animal["owner"]},format='text/html')     
        self.assertTrue(response.url == self.animal_url)
        self.assertEqual(response.status_code,302)

    def test_animal_form_without_login(self):
        response=self.client.post(self.animal_url,{'type':self.animal["type"],'genus':self.animal["genus"],'name':self.animal["name"],'age':self.animal["age"],'description':self.animal["description"],'owner':self.animal["owner"]},format='text/html')
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code,302)

    def test_animal_form_type_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.animal_url,{'type':self.animal_type_error["type"],'genus':self.animal["genus"],'name':self.animal["name"],'age':self.animal["age"],'description':self.animal["description"],'owner':self.animal["owner"]},format='text/html')
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code,302)

    def test_animal_form_genus_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.animal_url,{'type':self.animal["type"],'genus':self.animal_genus_error["genus"],'name':self.animal["name"],'age':self.animal["age"],'description':self.animal["description"],'owner':self.animal["owner"]},format='text/html')
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code,302)

    def test_animal_form_name_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.animal_url,{'type':self.animal["type"],'genus':self.animal["genus"],'name':self.animal_name_error["name"],'age':self.animal["age"],'description':self.animal["description"],'owner':self.animal["owner"]},format='text/html')
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code,302)

    def test_animal_form_description_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.animal_url,{'type':self.animal["type"],'genus':self.animal["genus"],'name':self.animal["name"],'age':self.animal["age"],'description':self.animal_description_error["description"],'owner':self.animal["owner"]},format='text/html')
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code,302)

class OwnerFormTest(BaseTest):

    def test_owner_form_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url == self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url == self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_without_login(self):
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_name_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.owner_url,{'name':self.animal_owner_name_error["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_surname_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner_surname_error["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_email_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner_email_error["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_phone_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner_phone_error["phone"],'address':self.animal_owner["address"]},format='text/html')     
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code,302)

    def test_owner_form_address_error(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response=self.client.post(self.owner_url,{'name':self.animal_owner["name"],'surname':self.animal_owner["surname"],'email':self.animal_owner["email"],'phone':self.animal_owner["phone"],'address':self.animal_owner_address_error["address"]},format='text/html')     
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code,302)
