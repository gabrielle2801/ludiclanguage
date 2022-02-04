from django.test import TestCase
# from faker import Faker
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from ludic_language.profiles.models import Profile
from ludic_language.exercises.models import Pathology

from freezegun import freeze_time
import datetime


class Profiletest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='LucasD', first_name='Lucas', password='12test12', email='test@email.com')
        self.user_id = self.user.pk
        self.user.save()
        self.therapist = User.objects.create_user(
            username='test', password='12test12').pk
        self.birth_date = datetime.date(2013, 12, 9)
        self.pathology_id = Pathology.objects.create(name='Dyslexie').pk
        Profile(user=self.user, birth_date=self.birth_date, state=1,
                bio='Lucas est atteint de ......', profile_pic='lucasdesmarais.png',
                pathology_id=self.pathology_id, therapist_id=self.therapist).save()

    @freeze_time("2022-01-14")
    def test_freeze_time(self):
        assert datetime.datetime.now() == datetime.datetime(2022, 1, 14)

    @freeze_time("2020-01-14")
    def test_age_valid(self):
        my_age = 6
        response = self.user.profile.age
        self.assertEquals(response, my_age)

    @freeze_time("2020-01-14")
    def test_age_invalid(self):
        my_age = 10
        response = self.user.profile.age
        self.assertNotEqual(response, my_age)

    def test_first_name_label(self):
        patient = User.objects.get(id=self.user_id)
        field_label = patient._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'prénom')

    def test_profile_username(self):
        self.assertEquals(self.user.__str__(), 'LucasD')
