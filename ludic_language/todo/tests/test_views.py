from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
# import datetime
from django.contrib.auth import get_user_model
from ludic_language.todo.models import Task


class TaskViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.form_url = reverse('task_form')
        self.client = Client()
        self.task = {
            'title': 'Tâche à faire',
            'description': 'Description de la tâche',
            'completed': True,
            'created_at': '2024-05-12 15:00',
            'due_datetime': '2024-06-12 15:00',
            'slug': 'Tâche à faire',
            'priority': 2,
            'therapist': self.user
        }
        return super().setUp()

    def test_view_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 200)

    def test_form_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.post(self.form_url, self.task)
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(title='Tâche à faire')
        task.description = 'Description de la tâche'


class TaskUpdateTest(TestCase):
    def test_update(self):
        therapist = User.objects.create_user(
            username='Marieaumont', password='12test12').pk
        task = Task.objects.create(title='Tâche à faire',
                                   description='Description de la tâche',
                                   completed=False,
                                   created_at='2024-05-12 15:00',
                                   due_datetime='2024-06-12 15:00',
                                   slug='Tâche à faire',
                                   priority=2,
                                   therapist_id=therapist)
        response = self.client.post(reverse('task_update', kwargs={
            'pk':  task.id}), {'completed': True})
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Tâche à faire')