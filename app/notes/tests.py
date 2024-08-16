from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Note

User = get_user_model()


class NoteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')
        self.note = Note.objects.create(user=self.user, name='Dog')
        self.list_url = reverse('notes:list_notes')
        self.add_url = reverse('notes:add_note')

    def test_note_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/list_notes.html')
        self.assertContains(response, self.note.name)

    def test_add_note(self):
        response = self.client.post(self.add_url, {'name': 'Cat'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(user=self.user, name='Cat').exists())

    def test_add_note_with_existing_name(self):
        response = self.client.post(self.add_url, {'name': 'Dog'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Note with this name already exists.')
