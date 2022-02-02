from django.test import TestCase
from django.http import HttpRequest
from ludic_language.profiles.forms import UserProfileForm
from django.contrib.auth.models import User
from ludic_language.profiles.models import Profile
from ludic_language.exercises.models import Pathology
from django.contrib.auth import get_user_model


class UserProfileFormTest(TestCase):
    def setUp(self):
        self.pathology_id = Pathology.objects.create(name='Dyslexie').pk
        self.therapist = User.objects.create_user(
            username='Marieaumont', password='Therapist@25').pk

        return super().setUp()

    def test_userprofile_valid(self):
        form = UserProfileForm(data={
            'first_name': 'Lucas',
            'last_name': 'Desmarais',
            'email': 'helenedesmarais@email.com',
            'username': 'LucasD',
            'password1': '12test12',
            'password2': '12test12',
            'birth_date': '2013-05-12',
            'bio': 'Lucas est atteint de ......',
            'profile_pic': 'lucasdesmarais.png',
            'pathology': self.pathology_id,
            'num': 10,
            'street': 'rue de la paix',
            'zip_code': 75015,
            'city': 'Paris',
        }, therapist=self.therapist)
        self.assertTrue(form.is_valid())
        profile = form.save()
        self.assertEquals(profile.username, 'LucasD')
