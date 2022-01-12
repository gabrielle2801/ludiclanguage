from django.contrib import admin
from ludic_language.profiles.models import User
from ludic_language.profiles.models import Address
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Address)
