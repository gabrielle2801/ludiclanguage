from django.db import models
from django.contrib.auth.models import AbstractUser
from extended_choices import Choices


STATES = Choices(
    ('PATIENT', 1, 'Patient'),
    ('SPEECH_PATHOLOGY', 2, 'Speech_Pathology'),
)


class User(AbstractUser):
    state = models.PositiveSmallIntegerField(
        choices=STATES, default=STATES.SPEECH_PATHOLOGY)
    bio = models.CharField(max_length=500, blank=True)
    review = models.CharField(max_length=500, blank=True, null=True)
    picture = models.ImageField(upload_to='pictures')


class Address(models.Model):
    num = models.IntegerField(null=True)
    street = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
