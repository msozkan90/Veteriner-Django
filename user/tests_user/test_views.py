
from django.urls import reverse
from django.test import TestCase

class ModelTest(TestCase):
    def setUp(self):
        self.register_url=reverse('user:register')
        self.signin_url=reverse('user:sign_in')
        self.signout_url=reverse('user:sign_out')

    def test_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'register.html')

    def test_signin(self):
        response = self.client.get(self.signin_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')

    def test_signout(self):
        response = self.client.get(self.signout_url)
        self.assertEqual(response.status_code, 302)



