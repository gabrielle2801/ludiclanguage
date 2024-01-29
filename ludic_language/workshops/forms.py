from django import forms
# from django.core.mail import send_mail

import os
from ludic_language.workshops.models import Workshop
from ludic_language.profiles.models import Profile

class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = ['patient', 'date', 'shedule_online']

    def __init__(self, *args, therapist=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist
        self.fields['patient'].queryset = Profile.objects.filter(
            therapist=self.therapist)

    def save(self, *args, **kwargs):
        self.instance.therapist = self.therapist
        return super().save(*args, **kwargs)


class ReportForm(forms.ModelForm):
    report = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Workshop
        fields = ['report']

    def __init__(self, *args, therapist=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist

    def save(self, *args, **kwargs):
        self.instance.therapist = self.therapist
        return super().save(*args, **kwargs)
    
    
