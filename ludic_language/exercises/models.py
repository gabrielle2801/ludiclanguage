from django.db import models
# from ludic_language.profiles.models import User


# Create your models here.


class Pathology(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    therapist_pathology = models.ForeignKey(
        'exercises.Pathology', on_delete=models.CASCADE, related_name='therapist_pathology', null=True, blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    picture1 = models.ImageField('picture1')
    picture2 = models.ImageField('picture2')
    therapist = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='therapist_exercice', null=True)
    pathology = models.ForeignKey(
        'Pathology', on_delete=models.CASCADE, null=True)


class LudicJourney(models.Model):
    journey_date = models.DateTimeField()
    assessement = models.CharField(max_length=200)
    patient = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='patient_ludicjourney', null=True)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
