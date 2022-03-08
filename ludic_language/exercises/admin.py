from django.contrib import admin
from ludic_language.exercises.models import Pathology, Exercise
from ludic_language.profiles.models import Profile

admin.site.register(Pathology)
admin.site.register(Exercise)
