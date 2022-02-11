from django.test import TestCase
from ludic_language.profiles.models import User
from ludic_language.workshops.models import Workshop
from django.contrib.auth import get_user_model


class WorkshopTest(TestCase):
    def setUp(self):
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', email='test@email.com').pk
        self.workshop = Workshop.objects.create(
            date='2022-02-12 15:00', shedule_online='https://meet.google.com/njy-iipe-rkp',
            patient_id=self.patient, therapist_id=self.therapist).pk

    def test_shedule_online(self):
        workshop = Workshop.objects.get(id=self.workshop)
        field_label = workshop._meta.get_field('shedule_online').verbose_name
        self.assertEquals(field_label, 'shedule online')
