from django.test import TestCase
from ludic_language.profiles.forms import UserProfileForm
from django.contrib.auth.models import User
from ludic_language.exercises.models import Pathology


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
            'review': 'Bilan du patient .....',
            'profile_pic': 'lucasdesmarais.png',
            'pathology': self.pathology_id,
            'num': 10,
            'street': 'rue de la paix',
            'zip_code': 75015,
            'city': 'Paris',
        }, therapist=self.therapist)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_userprofile_missing_first_name(self):
        form = UserProfileForm(data={
            'first_name': '',
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
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_userprofile_missing_email_invalid(self):
        form = UserProfileForm(data={
            'first_name': 'Lucas',
            'last_name': 'Desmarais',
            'email': 'helenedesmaraisemail.com',
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
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_userprofile_password_invalid(self):
        form = UserProfileForm(data={
            'first_name': 'Lucas',
            'last_name': 'Desmarais',
            'email': 'helenedesmarais@email.com',
            'username': 'LucasD',
            'password1': '12test12',
            'password2': '12test',
            'birth_date': '2013-05-12',
            'bio': 'Lucas est atteint de ......',
            'profile_pic': 'lucasdesmarais.png',
            'pathology': self.pathology_id,
            'num': 10,
            'street': 'rue de la paix',
            'zip_code': 75015,
            'city': 'Paris',
        }, therapist=self.therapist)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
