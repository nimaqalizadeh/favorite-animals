from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class AccountViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')
        self.login_url = reverse('accounts:login')
        self.logout_url = reverse('accounts:logout')
        self.username = 'test_user'
        self.password = 'test_password'

    def test_register_view_success(self):
        response = self.client.post(self.register_url, {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('notes:list_notes'))
        self.assertTrue(User.objects.filter(username=self.username).exists())

    def test_register_view_failure(self):
        response = self.client.post(self.register_url, {
            'username': 'wrong_user',
            'password1': 'test_password',
            'password2': 'wrrong_test_password',
        })
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(User.objects.filter(username='wrong_user').exists())

    def test_login_view_success(self):
        User.objects.create_user(username=self.username, password=self.password)
        
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('notes:list_notes'))

    def test_login_view_failure(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrong_test_password',
        })
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "Please enter a correct username and password")

    def test_logout_view(self):
        user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertNotIn('_auth_user_id', self.client.session)
