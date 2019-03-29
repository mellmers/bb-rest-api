from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import *


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'url', 'created_at', 'updated_at', 'bio', 'birth_date', 'city', 'country', 'clan', 'games',
            'gamertag', 'logo')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'profile', 'groups')
