from django.db import models
from ludic_language.profiles.models import User


# Create your models here.


class Pathology(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)


class Exercise(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    picture1 = models.ImageField('picture1')
    picture2 = models.ImageField('picture2')
    pathology = models.ForeignKey(Pathology, on_delete=models.CASCADE)


class ludic_journey(models.Model):
    journey_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    assessement = models.CharField(max_length=200)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
