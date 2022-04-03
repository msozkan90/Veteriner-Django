from django.urls import reverse
from django.test import TestCase


class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('user:register')
        self.login_url=reverse('user:sign_in')
        self.user={
            'email':'example123@gmail.com',
            'username':'example11',
            'password':'PassWord*123',
            'password2':'PassWord*123',
            'name':'Example'
        }
        self.user_short_password={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'tes',
            'password2':'tes',
            'name':'fullname'
        }
        self.user_unmatching_password={

            'email':'testemail@gmail.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
            'name':'fullname'
        }

        self.user_invalid_email={
            
            'email':'test.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
            'name':'fullname'
        }

        return super().setUp()

class RegisterTest(BaseTest):

   def test_can_register_user(self):
        response=self.client.post(self.register_url,{'password1':self.user["password"],'password2':self.user["password2"],'username':self.user["username"],'email':self.user["email"]},format='text/html')
        self.assertTrue(response.url == self.login_url)
        self.assertEqual(response.status_code,302)

   def test_cant_register_user_withshortpassword(self):
        response=self.client.post(self.register_url,{'password':self.user_short_password["password"],'password2':self.user_short_password["password2"],'username':self.user_short_password["username"],'email':self.user_short_password["email"]},format='text/html')
        self.assertTrue(response.url == self.register_url)
        self.assertEqual(response.status_code,302)

   def test_cant_register_user_with_unmatching_passwords(self):
        response=self.client.post(self.register_url,self.user_unmatching_password,format='text/html')
        self.assertTrue(response.url == self.register_url)
        self.assertEqual(response.status_code,302)

   def test_cant_register_user_with_invalid_email(self):
        response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
        self.assertTrue(response.url == self.register_url)
        self.assertEqual(response.status_code,302)

   def test_cant_register_user_with_taken_email(self):
        self.client.post(self.register_url,self.user,format='text/html')
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertTrue(response.url == self.register_url)
        self.assertEqual(response.status_code,302)



class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def test_login_success(self):
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

    def test_cantlogin_with_wrong_username(self):
        response= self.client.post(self.login_url,{'password':'passgfghfhfword','username':'wrongusername'},format='text/html')
        self.assertTrue(response.url == self.login_url)
        self.assertEqual(response.status_code,302)

    def test_cantlogin_with_wrong_password(self):
        response= self.client.post(self.login_url,{'password':'wrongpassword','username':'username'},format='text/html')
        self.assertTrue(response.url == self.login_url)
        self.assertEqual(response.status_code,302)

    def test_cantlogin_with_empty_password(self):
        response= self.client.post(self.login_url,{'password':'','username':'username'},format='text/html')
        self.assertTrue(response.url == self.login_url)
        self.assertEqual(response.status_code,302)

    def test_cantlogin_with_empty_username(self):
        response= self.client.post(self.login_url,{'password':'password','username':''},format='text/html')
        self.assertTrue(response.url == self.login_url)
        self.assertEqual(response.status_code,302)





























