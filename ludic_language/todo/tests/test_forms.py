from django.test import TestCase
from django.contrib.auth.models import User
from ludic_language.todo.forms import TaskCreateForm


class TaskCreateFormTest(TestCase):
    def setUp(self):
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk

        return super().setUp()
    
    def test_task_valid(self):
        form = TaskCreateForm(data={
            'title': 'Tâche à faire',
            'description': 'Description de la tâche',
            'completed': True,
            'created_at': '2024-05-12 15:00',
            'due_datetime': '2024-06-12 15:00',
            'slug': 'title',
            'priority': 2,
        }, therapist=self.therapist)
        self.assertTrue(form.is_valid())

    def test_task_valid_missing_title(self):
        form = TaskCreateForm(data={
            'title': '',
            'description': 'Description de la tâche',
            'completed': True,
            'created_at': '2024-05-12 15:00',
            'due_datetime': '2024-06-12 15:00',
            'slug': 'title',
            'priority': 2,
        }, therapist=self.therapist)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_task_date_error(self):
        form = TaskCreateForm(data={
            'title': '',
            'description': 'Description de la tâche',
            'completed': True,
            'created_at': '2024-05-12 15:00',
            'due_datetime': '2023-06-12 15:00',
            'slug': 'title',
            'priority': 2,
        }, therapist=self.therapist)
        self.assertFalse(form.is_valid())
        self.assertIn('due_datetime', form.errors)