# Generated by Django 4.1.7 on 2023-03-21 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0014_recordermessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordermessage',
            name='game',
        ),
        migrations.AddField(
            model_name='recordermessage',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_recorder', to='exercises.exercise'),
        ),
    ]