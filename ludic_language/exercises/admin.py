from django.contrib import admin
from ludic_language.exercises.models import (Pathology,
                                             Exercise,
                                             RecorderMessage,
                                             LudicJourney)


admin.site.register(Pathology)
admin.site.register(Exercise)
admin.site.register(RecorderMessage)
admin.site.register(LudicJourney)
