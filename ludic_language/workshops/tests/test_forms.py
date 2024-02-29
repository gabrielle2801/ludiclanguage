from django.test import TestCase
from ludic_language.workshops.forms import WorkshopForm, ReportForm
from ludic_language.workshops.models import Workshop
from django.contrib.auth.models import User


class WorkshopFormTest(TestCase):
    def setUp(self):
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='LucasDes', 
            email='test@email.com', password='12test12').pk
        return super().setUp()

    def test_workshop_valid(self):
        form = WorkshopForm(data={
            'date': '2022-02-12 15:00',
            'shedule_online': 'https://meet.google.com/njy-iipe-rkp',
            'patient': self.patient,
            'therapist': self.therapist
        })
        self.assertTrue(form.is_valid())

    def test_workshop_invalid_date(self):
        form = WorkshopForm(data={
            'date': '2022-02-12 15/00',
            'shedule_online': 'https://meet.google.com/njy-iipe-rkp',
            'patient': self.patient,
            'therapist': self.therapist
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_workshop_invalid_link(self):
        form = WorkshopForm(data={
            'date': '2022-02-12 15:00',
            'shedule_online': '',
            'patient': self.patient,
            'therapist': self.therapist
        })
        self.assertFalse(form.is_valid())
        self.assertIn('shedule_online', form.errors)


class ReformFormTest(TestCase):
    def setUp(self):
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='LucasDes', 
            email='test@email.com', password='12test12').pk
        self.workshop = Workshop.objects.create(
            date='2022-02-12 15:00', 
            shedule_online='https://meet.google.com/njy-iipe-rkp',
            patient_id=self.patient, therapist_id=self.therapist).pk
        return super().setUp()

    def test_form_valid(self):
        form = ReportForm(data={
            'report': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
            'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        })
        self.assertTrue(form.is_valid())
