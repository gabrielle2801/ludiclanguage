from django.db import models
# from ludic_language.profiles.models import User


# Create your models here.


class Pathology(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    title_game = models.CharField(max_length=500, blank=True)
    description_game = models.TextField(blank=True)
    picture1 = models.ImageField('picture1', blank=True)
    picture2 = models.ImageField('picture2', blank=True)
    therapist = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='therapist_exercice', null=True, blank=True)
    pathology = models.ForeignKey(
        'Pathology', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title_game


class LudicJourney(models.Model):
    journey_date = models.DateTimeField(null=True, blank=True)
    assessement = models.CharField(max_length=200, null=True, blank=True)
    patient = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='patient_ludicjourney', null=True)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)


'''
L'aider à apprendre et identifier des lettres facilement.
Les exercices de traitement visuel permettent d'améliorer la capacité de votre enfant à distinguer les différences entre plusieurs objets.
Puzzle : Assembler les morceaux afin de reproduire l'image.
'''
