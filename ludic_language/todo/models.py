from django.db import models
from django.utils import timezone
from extended_choices import Choices

# Create your models here.

PRIORITY = Choices(
    ('LOW', 1, 'Low'),
    ('MEDIUM', 2, 'Medium'),
    ('HIGH', 3, 'High'),
)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY, default=PRIORITY.LOW, null=True, blank=True)
    therapist = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE,
        related_name='therapist_todo',  null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']
