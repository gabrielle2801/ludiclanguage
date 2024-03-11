from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from ludic_language.todo.models import Task


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority',
                  'completed', 'due_datetime')
        widgets = {
            'due_datetime': DateTimeInput,
        }

    def clean_due_datetime(self):
        """
        Valid a futur datetime task
        """
        due_datetime = self.cleaned_data["due_datetime"]
        now = timezone.now()
        if due_datetime < now:
            raise ValidationError(
                "The date must be in the furtur !"
            )
        return due_datetime

    def __init__(self, *args, therapist=None, ** kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist

    def save(self, *args, **kwargs):
        self.instance.therapist = self.therapist
        return super().save(*args, **kwargs)
