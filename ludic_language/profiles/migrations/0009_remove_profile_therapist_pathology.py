# Generated by Django 4.0.2 on 2022-03-08 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_therapist_pathology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='therapist_pathology',
        ),
    ]
