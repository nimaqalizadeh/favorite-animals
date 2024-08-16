from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ...models import Animal

User = get_user_model()


class AnimalAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password') 
        self.animal = Animal.objects.create(user=self.user, name='Dog')
        self.animal_url = reverse('animals:api-v1:animal_detail', kwargs={'pk': self.animal.pk})
        self.animal_list_url = reverse('animals:api-v1:animal_create')

    def test_create_animal(self):
        data = {'name': 'Cat'}
        response = self.client.post(self.animal_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Animal.objects.count(), 2)
        self.assertEqual(Animal.objects.get(id=response.data['id']).name, 'Cat')

    def test_create_animal_with_existing_name(self):
        data = {'name': 'Dog'}
        response = self.client.post(self.animal_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'The animal with this name already exists.')

    def test_retrieve_animal(self):
        response = self.client.get(self.animal_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Dog')

    def test_update_animal(self):
        data = {'name': 'Wolf'}
        response = self.client.put(self.animal_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.animal.refresh_from_db()
        self.assertEqual(self.animal.name, 'Wolf')

    def test_delete_animal(self):
        response = self.client.delete(self.animal_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Animal.objects.count(), 0)
