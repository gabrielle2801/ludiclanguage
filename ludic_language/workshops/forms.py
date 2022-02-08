from django import forms
from django.core.mail import send_mail
from ludic_language.workshops.models import Workshop
from ludic_language.profiles.models import User, Profile


class WorkshopForm(forms.ModelForm):
    date = forms.DateTimeField()
    shedule_online = forms.URLField()
    patient = forms.ModelChoiceField(
        queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, therapist=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist
        self.fields['patient'].queryset = Profile.objects.filter(
            therapist_id=self.therapist)

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        workshop = Workshop.objects.create(
            date=self.cleaned_data['date'], shedule_online=self.cleaned_data['shedule_online'],
            patient_id=self.cleaned_data['patient'], therapist_id=self.user)
        user.workshop.save()
        return user

    def send_email(self):
        # patient = form.cleaned_data['first_name']

        send_mail(
            'Prochaine Session',
            'lien de votre prochaine session',
            'gabrielleazadian@gmail.com',
            ['xav_82@msn.com'],
            fail_silently=False
        )
