from django.db import models
from extended_choices import Choices
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.db.models.signals import post_save


STATES = Choices(
    ('PATIENT', 1, 'Patient'),
    ('SPEECH_THERAPIST', 2, 'Speech_Therapist'),
)

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    state = models.PositiveSmallIntegerField(
        choices=STATES, default=STATES.SPEECH_THERAPIST)
    bio = models.TextField(max_length=500, blank=True)
    review = models.CharField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='pictures/', blank=True)
    therapist = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    pathology = models.ForeignKey(
        'exercices.Pathology', on_delete=models.CASCADE, related_name='patient_pathology', null=True)


class Address(models.Model):
    num = models.IntegerField(null=True)
    street = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    profile = models.OneToOneField(
        'UserProfile', on_delete=models.CASCADE)


def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)
