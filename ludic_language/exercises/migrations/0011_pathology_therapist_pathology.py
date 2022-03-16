# Generated by Django 4.0.2 on 2022-03-08 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_alter_ludicjourney_assessement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathology',
            name='therapist_pathology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='therapist_path', to='exercises.pathology'),
        ),
    ]