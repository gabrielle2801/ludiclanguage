# Generated by Django 4.0 on 2021-12-17 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('shedule_online', models.URLField()),
                ('report', models.CharField(max_length=500)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='profiles.user')),
                ('speech_therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speech_therapist', to='profiles.user')),
            ],
        ),
    ]
