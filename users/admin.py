from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'birth_date', 'city', 'country', 'clan', 'games', 'gamertag', 'logo', 'updated_at', 'created_at')
    list_display_links = ('id', 'user')
    list_filter = ('clan', 'city', 'country')
    search_fields = ('bio', 'birth_date', 'city', 'country', 'clan', 'games', 'gamertag')


admin.site.register(Profile, ProfileAdmin)
