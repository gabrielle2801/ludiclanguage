# Generated by Django 5.0.1 on 2024-01-16 08:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(blank=True, max_length=5, null=True)),
                ('state', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Patient'), (2, 'Speech_Therapist'), (3, 'Admin')], default=1, null=True)),
                ('bio', models.TextField(blank=True)),
                ('review', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='par_defaut.png', null=True, upload_to='pictures/')),
                ('pathology', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_pathology', to='exercises.pathology')),
                ('therapist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(null=True)),
                ('street', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, max_length=5)),
                ('city', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
