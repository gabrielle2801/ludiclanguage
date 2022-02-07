from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from ludic_language.profiles.models import Profile
from ludic_language.exercises.models import Pathology


class UserProfileViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Marieaumont', password='Therapist@25').pk

        self.patient = User.objects.create_user(
            username='ClarenceBr', password='12test12', email='test@email.com')
        self.pathology_id = Pathology.objects.create(name='Dyslexie').pk
        self.form_url = reverse('form_patient')
        self.client = Client()
        self.patient = {
            'first_name': 'Clarence',
            'last_name': 'Brault',
            'username': 'ClarenceBr',
            'email': 'test@email.com',
            'password1': '12test12',
            'password2': '12test12',
            'birth_date': '12/05/2013',
            'bio': 'Clarence est atteint de ......',
            'profile_pic': '',
            'pathology': self.pathology_id,
            'num': '10',
            'street': 'rue de la paix',
            'zip_code': '75015',
            'city': 'Paris',
            'therapist': self.user
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
        response = self.client.post(self.form_url, self.patient)
        self.assertEquals(response.status_code, 200)
        patient = User.objects.get(email='test@email.com')
        patient.pathology_id = self.pathology_id
        patient.first_name = 'Clarence'


class PatientDetailTest(TestCase):

    def test_status_code_200(self):
        def setUp(self):
            self.user = get_user_model().objects.create_user(
                username='LucasD', password='12test12', email='test@email.com').pk
            self.therapist = User.objects.create_user(
                username='test', password='12test12').pk
            self.pathology_id = Pathology.objects.create(name='Dyslexie').pk
            self.profile = Profile.objects.create(user_id=self.user, birth_date='2013-05-12', state=1,
                                                  bio='Lucas est atteint de ......', profile_pic='lucasdesmarais.png',
                                                  pathology_id=self.pathology_id, therapist_id=self.therapist)
            self.profile.save()
            return super().setUp()

        def test_detail(self):
            detail_url = reverse('detail_patient', kwargs={
                'pk': self.profile})
            response = self.client.get(detail_url)
            assert response.status_code == 200
            self.assertTemplateUsed(response, 'detail_patient.html')


class PatientDeleteTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='LucasD', first_name='Lucas', password='12test12', email='test@email.com')
        self.user_id = self.user.pk
        self.user.save()
        self.therapist = User.objects.create_user(
            username='test', password='12test12').pk

        self.pathology_id = Pathology.objects.create(name='Dyslexie').pk
        Profile(user=self.user, birth_date='2013-05-12', state=1,
                bio='Lucas est atteint de ......', profile_pic='lucasdesmarais.png',
                pathology_id=self.pathology_id, therapist_id=self.therapist).save()

    def test_delete_valid(self):
        login = self.client.login(
            username='test', password='12test12')
        self.assertTrue(login)
        delete_url = reverse('delete_patient', kwargs={
            'pk': self.user_id})

        response = self.client.get(delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient_confirm_delete.html')
