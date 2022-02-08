from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail

from django.contrib.auth.models import User
from ludic_language.workshops.models import Workshop
# from ludic_language.workshops.forms import WorkshopForm


class UserProfileViewTest(TestCase):
    def setUp(self):
        self.therapist = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk
        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', email='test@email.com').pk
        self.form_url = reverse('form_workshop')
        self.client = Client()
        self.workshop = {
            'date': '2022-02-12',
            'shedule_online': 'https://meet.google.com/njy-iipe-rkp',
            'patient': self.patient,
            'therapist': self.therapist
        }

        return super().setUp()

    def test_view_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.get(self.form_url)
        self.assertEquals(response.status_code, 200)

    def test_form_ok(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25')
        self.assertTrue(login)
        response = self.client.post(self.form_url, self.workshop)
        self.assertEquals(response.status_code, 200)

    def test_send_email(self):
        login = self.client.login(
            username='Marieaumont', password='Therapist@25', email='therapist@email.com')
        self.assertTrue(login)
        mail.send_mail(
            'Rendez-vous session', 'lien vers visio',
            'therapist@email.com', ['test@email.com'],
            fail_silently=False,
        )
        self.assertEquals(mail.outbox[0].subject, 'Rendez-vous session')
