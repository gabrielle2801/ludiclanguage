from django.test import TestCase
from ludic_language.workshops.forms import WorkshopForm
# from ludic_language.workshops.models import Workshop
from django.contrib.auth.models import User


class WorkshopFormTest(TestCase):
    def setUp(self):
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='LucasDes', email='test@email.com', password='12test12')
        return super().setUp()

    def test_workshop_valid(self):
        form = WorkshopForm(data={
            'email': self.patient.email,
            'date': '2022-02-12',
            'shedule_online': 'https://meet.google.com/njy-iipe-rkp',
            'patient': self.patient
        })
        self.assertTrue(form.is_valid())
