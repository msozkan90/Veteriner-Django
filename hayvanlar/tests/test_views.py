
from django.urls import reverse
from django.test import TestCase
from hayvanlar.models import AnimalOwners, Animals
from django.contrib.auth.models import User

USERNAME_1="example"
PASSWORD_1="example12345"
USERNAME_SUPER="examplesuper"
PASSWORD_SUPER="examplesuper12345"

class ModelTest(TestCase):
    def setUp(self):
        self.animal_url=reverse('hayvanlar:animals')
        self.owner_url=reverse('hayvanlar:animalowners')
        owner= AnimalOwners.objects.create(name="Example",surname="Example",address="Example",email="example@gmail.com",phone="05555555555")
        animal = Animals.objects.create(type="Example",genus="Example",name="Example",age="2",owner=owner,description="Example")
        self.test_user = User.objects.create_user(USERNAME_1, 'example@gmail.com', PASSWORD_1)
        self.test_superuser = User.objects.create_superuser(USERNAME_SUPER, 'example1@gmail.com', PASSWORD_SUPER,)
        self.list_animal_url=reverse('hayvanlar:animals')
        self.list_owner_url=reverse('hayvanlar:animalowners')
        self.delete_animal_url=reverse('hayvanlar:animal_delete',args=['1'])
        self.delete_owner_url=reverse('hayvanlar:owner_delete',args=['1'])
        self.edit_animal_url=reverse('hayvanlar:animal-update',args=['1'])
        self.edit_owner_url=reverse('hayvanlar:owner-update',args=['1'])
        self.detail_animal_url=reverse('hayvanlar:animal_detail',args=['1'])
        self.detail_owner_url=reverse('hayvanlar:owner_detail',args=['1'])

    def test_index(self):
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

#ANIMAL PAGE TESTS
    def test_animal_list_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.list_animal_url)
        self.assertEqual(response.status_code, 200)

    def test_animal_list_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.list_animal_url)
        self.assertEqual(response.status_code, 200)

    def test_animal_list_without_user(self):
        response = self.client.get(self.list_animal_url)
        self.assertEqual(response.status_code, 302)

    def test_animal_detail_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.detail_animal_url)
        self.assertEqual(response.status_code, 200)

    def test_animal_detail_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.detail_animal_url)
        self.assertEqual(response.status_code, 200)

    def test_animal_detail_without_user(self):
        response = self.client.get(self.detail_animal_url)
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code, 302)

    def test_animal_edit_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)        
        response = self.client.get(self.edit_animal_url)
        self.assertEqual(response.status_code, 200)

    def test_animal_edit_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)        
        response = self.client.get(self.edit_animal_url)
        self.assertEqual(response.status_code, 302)

    def test_animal_edit_without_user(self):    
        response = self.client.get(self.edit_animal_url)
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code, 302)

    def test_animal_delete_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.delete_animal_url)
        self.assertTrue(response.url == self.animal_url)
        self.assertEqual(response.status_code, 302)

    def test_animal_delete_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.delete_animal_url)
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code, 302)

    def test_animal_delete_without_user(self):
        response = self.client.get(self.delete_animal_url)
        self.assertTrue(response.url != self.animal_url)
        self.assertEqual(response.status_code, 302)



#OWNER PAGE TESTS
    def test_owner_list_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.list_owner_url)
        self.assertEqual(response.status_code, 200)

    def test_owner_list_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.list_owner_url)
        self.assertEqual(response.status_code, 200)

    def test_owner_list_without_user(self):
        response = self.client.get(self.list_owner_url)
        self.assertEqual(response.status_code, 302)

    def test_owner_delete_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.delete_owner_url)
        self.assertTrue(response.url == self.owner_url)
        self.assertEqual(response.status_code, 302)

    def test_owner_delete_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.delete_owner_url)
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code, 302)

    def test_owner_delete_without_user(self):
        response = self.client.get(self.delete_owner_url)
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code, 302)

    def test_owner_edit_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.edit_owner_url)
        self.assertEqual(response.status_code, 200)

    def test_owner_edit_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.edit_owner_url)
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code, 302)

    def test_owner_edit_without_user(self):
        response = self.client.get(self.edit_owner_url)
        self.assertTrue(response.url != self.owner_url)
        self.assertEqual(response.status_code, 302)

    def test_owner_detail_superuser(self):
        self.client.login(username=USERNAME_SUPER, password=PASSWORD_SUPER)
        response = self.client.get(self.detail_owner_url)
        self.assertEqual(response.status_code, 200)

    def test_owner_detail_normaluser(self):
        self.client.login(username=USERNAME_1, password=PASSWORD_1)
        response = self.client.get(self.detail_owner_url)
        self.assertEqual(response.status_code, 200)

    def test_owner_detail_without_user(self):
        response = self.client.get(self.detail_owner_url)
        self.assertEqual(response.status_code, 302)