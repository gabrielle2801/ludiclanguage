from django.test import TestCase
from ludic_language.workshops.forms import WorkshopForm
from ludic_language.workshops.models import Workshop
from django.contrib.auth.models import User


class WorkshopFormTest(TestCase):
    def setUp(self):
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='LucasDes', password='12test12').pk
        return super().setUp()

    def test_workshop_valid(self):
        form = WorkshopForm(data={
            'username': 'LucasDes',
            'email': 'helenedesmarais@email.com',
            'date': '2022-02-12',
            'shedule_online': 'https://meet.google.com/njy-iipe-rkp',
        })
        self.assertTrue(form.is_valid())
