from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Animal

User = get_user_model()


class AnimalViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')
        self.animal = Animal.objects.create(user=self.user, name='Dog')
        self.list_url = reverse('animals:list_animals')
        self.add_url = reverse('animals:add_animal')

    def test_animal_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/list_animals.html')
        self.assertContains(response, self.animal.name)

    def test_add_animal(self):
        response = self.client.post(self.add_url, {'name': 'Cat'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Animal.objects.filter(user=self.user, name='Cat').exists())

    def test_add_animal_with_existing_name(self):
        response = self.client.post(self.add_url, {'name': 'Dog'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Animal with this name already exists.')
