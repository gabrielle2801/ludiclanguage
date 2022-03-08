# Generated by Django 4.0.2 on 2022-02-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_remove_pathology_therapist'),
        ('profiles', '0006_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='therapist_pathology',
            field=models.ManyToManyField(blank=True, null=True, to='exercises.Pathology'),
        ),
    ]