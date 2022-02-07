from django import forms
from ludic_language.workshops.models import Workshop
# from ludic_language.profiles.models import User


class WorkshopForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    date = forms.DateTimeField(required=True)
    shedule_online = forms.URLField()

    class Meta:
        model = Workshop
        fields = ['username', 'email', 'date', 'shedule_online']

    def __init__(self, *args, patient=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.patient = patient

    def save(self, *args, **kwargs):
        workshop = super().save(*args, **kwargs)
        workshop.user.patient = self.patient
        workshop.user.save()
        return workshop
