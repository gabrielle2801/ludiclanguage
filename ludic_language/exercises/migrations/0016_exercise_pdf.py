# Generated by Django 4.1.7 on 2023-05-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0015_remove_recordermessage_game_recordermessage_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdf'),
        ),
    ]
