from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ...models import Note

User = get_user_model()


class NoteAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password') 
        self.note = Note.objects.create(user=self.user, name='Dog')
        self.note_url = reverse('notes:api-v1:note_detail', kwargs={'pk': self.note.pk})
        self.note_list_url = reverse('notes:api-v1:note_create')

    def test_create_note(self):
        data = {'name': 'Cat'}
        response = self.client.post(self.note_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(Note.objects.get(id=response.data['id']).name, 'Cat')

    def test_create_note_with_existing_name(self):
        data = {'name': 'Dog'}
        response = self.client.post(self.note_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'The note with this name already exists.')

    def test_retrieve_note(self):
        response = self.client.get(self.note_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Dog')

    def test_update_note(self):
        data = {'name': 'Wolf'}
        response = self.client.put(self.note_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.name, 'Wolf')

    def test_delete_note(self):
        response = self.client.delete(self.note_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
