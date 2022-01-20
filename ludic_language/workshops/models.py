from django.db import models
# from ludic_language.profiles.models import User


class Workshop(models.Model):
    date = models.DateTimeField()
    shedule_online = models.URLField(max_length=200)
    report = models.CharField(max_length=500)
    patient = models.ForeignKey(
        'profiles.UserProfile', on_delete=models.CASCADE, related_name='patient_workshop', null=True)
    therapist = models.ForeignKey(
        'profiles.UserProfile', on_delete=models.CASCADE, related_name='therapist_workshop', null=True)
