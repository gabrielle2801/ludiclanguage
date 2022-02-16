from django.db import models
# from ludic_language.profiles.models import User


class Workshop(models.Model):
    date = models.DateTimeField()
    shedule_online = models.URLField(max_length=200)
    report = models.CharField(max_length=500, blank=True)
    patient = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='patient_workshop', null=True)
    therapist = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='therapist_workshop', null=True)

    @property
    def report_done(self):
        if self.report == '':
            return False
        else:
            return True
