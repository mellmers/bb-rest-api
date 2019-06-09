from django.db import models
import django.utils.timezone


class Match(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=django.utils.timezone.now)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_time = models.DateTimeField(default=django.utils.timezone.now)
    description = models.CharField(max_length=500, null=True, blank=True)
    matches = models.ManyToManyField(Match)

    def __str__(self):
        return self.name
