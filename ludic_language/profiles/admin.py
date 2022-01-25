from django.contrib import admin
from ludic_language.profiles.models import User, Profile
from ludic_language.profiles.models import Address
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Address)
