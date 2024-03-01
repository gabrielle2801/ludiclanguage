# Generated by Django 5.0.2 on 2024-03-01 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('todo', '0003_alter_task_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='patient',
        ),
        migrations.AlterField(
            model_name='task',
            name='therapist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='therapist_todo', to='profiles.profile'),
        ),
    ]
