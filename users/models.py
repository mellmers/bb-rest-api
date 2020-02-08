from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    bio = models.TextField(max_length=5000, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    clan = models.CharField(max_length=255, blank=True)
    games = models.CharField(max_length=255, blank=True)
    gamertag = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username + "---" + self.user.first_name + " " + self.user.last_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
