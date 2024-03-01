from django import forms
from ludic_language.exercises.models import LudicJourney, Exercise
from ludic_language.profiles.models import Profile


class LudicJourneyCreateForm(forms.ModelForm):

    class Meta:
        model = LudicJourney
        fields = ['journey_date', 'patient', 'exercise']

    def __init__(self, *args, therapist=None, patient=None, ** kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist
        self.patient = patient
        self.fields['patient'].queryset = Profile.objects.filter(
            therapist=self.therapist)
        self.fields['exercise'].queryset = Exercise.objects.all()


class LudicJourneyAssessementForm(forms.ModelForm):
    assessement = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = LudicJourney
        fields = ['assessement']

    def __init__(self, *args, therapist=None, patient=None,
                 exercise=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist
        self.exercise = exercise
        self.patient = patient

    def save(self, *args, **kwargs):
        self.instance.therapist = self.therapist
        return super().save(*args, **kwargs)
