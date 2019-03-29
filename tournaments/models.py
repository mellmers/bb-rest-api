from django.db import models


class Match(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    matches = models.ManyToManyField(Match)

    def __str__(self):
        return self.name

