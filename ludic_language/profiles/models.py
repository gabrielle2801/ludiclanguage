from django.db import models
from extended_choices import Choices
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


STATES = Choices(
    ('PATIENT', 1, 'Patient'),
    ('SPEECH_THERAPIST', 2, 'Speech_Therapist'),
    ('ADMIN', 3, 'Admin'),
)

# User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField(max_length=5, null=True, blank=True)
    state = models.PositiveSmallIntegerField(
        choices=STATES, default=STATES.PATIENT, null=True, blank=True)
    bio = models.TextField(blank=True)
    review = models.CharField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='pictures/', blank=True, null=True, default='par_defaut.png')
    therapist = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, null=True, blank=True)
    pathology = models.ForeignKey(
        'exercises.Pathology', on_delete=models.CASCADE, related_name='patient_pathology', null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def age(self):
        birth_date = self.birth_date
        today = datetime.date.today()
        my_age = (today.year - birth_date.year) - \
            int((today.month, today.day) < (birth_date.month, birth_date.day))
        return my_age


class Address(models.Model):
    num = models.IntegerField(null=True)
    street = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    profile = models.OneToOneField(
        'Profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile.user)


@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()


post_save.connect(create_user_profile, sender=User)
