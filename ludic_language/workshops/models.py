from django.db import models
from ludic_language.profiles.models import User


class Workshop(models.Model):
    date = models.DateTimeField()
    shedule_online = models.URLField(max_length=200)
    report = models.CharField(max_length=500)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    speech_therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='speech_therapist')
