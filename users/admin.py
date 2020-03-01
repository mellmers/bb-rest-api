from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import GroupAdmin

from .models import *
from .models import User
from .forms import RegisterForm, UserAddForm, UserUpdateForm


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,                  {'fields': ('username', 'password')}),
        ('Administration',      {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups')}),
        ('User info',           {'fields': ('first_name', 'last_name', 'email', 'bio', 'birth_date', 'city', 'country', 'clan', 'games', 'logo')}),
        ('Date info',   {'fields': ('last_login', 'updated_at', 'created_at')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = UserUpdateForm
    add_form = UserAddForm
    change_password_form = auth_admin.AdminPasswordChangeForm

    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'bio', 'birth_date', 'city', 'country', 'clan', 'games', 'logo', 'last_login', 'updated_at', 'created_at']
    list_display_links = ['id', 'username', 'first_name', 'last_name', 'email']
    list_filter = ['clan', 'city', 'country', 'last_login', 'updated_at', 'created_at']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'birth_date', 'city', 'country', 'clan', 'games']

    readonly_fields = ['last_login', 'updated_at', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
