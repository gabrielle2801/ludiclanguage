from django.db import models
from django.utils import timezone
from extended_choices import Choices
from django_extensions.db.fields import AutoSlugField

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
    due_datetime = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(populate_from=["title"])
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY, default=PRIORITY.LOW, null=True, blank=True)
    therapist = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE,
        related_name='therapist_todo',  null=True)

    def __str__(self):
        return f"{self.title} (due le {self.due_datetime.strftime('%d/%m/%Y à %H:%M')})"

    class Meta:
        ordering = ['priority']
