# Generated by Django 4.0.3 on 2022-03-24 11:13

from django.db import migrations


def create_pathologies(apps, schema_editor):
    Pathology = apps.get_model('exercises', 'Pathology')
    Pathology.objects.get_or_create(name='test', description="test ....")


def reverse_pathologies(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0011_pathology_therapist_pathology'),
    ]

    operations = [
        migrations.RunPython(create_pathologies, reverse_pathologies),
    ]
