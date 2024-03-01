from django import forms
from ludic_language.todo.models import Task


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority',
                  'completed', 'created_at']

    def __init__(self, *args, therapist=None, ** kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist

    def save(self, *args, **kwargs):
        self.instance.therapist = self.therapist
        return super().save(*args, **kwargs)
