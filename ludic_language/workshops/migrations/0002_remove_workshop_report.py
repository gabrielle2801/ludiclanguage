# Generated by Django 4.0.2 on 2022-02-16 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='report',
        ),
    ]
