from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as AbstractGroup

from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    bio = models.TextField(max_length=5000, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    clan = models.CharField(max_length=255, null=True, blank=True)
    games = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    # gamertag = models.CharField(max_length=255) # Steam name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username + (" (" + self.first_name + " " + self.last_name + ")" if self.first_name and self.last_name else "")

    def clean(self):
        if self.email == "":
            self.email = None


class Group(AbstractGroup):
    notes = models.TextField(blank=True)

    objects = models.Manager()
