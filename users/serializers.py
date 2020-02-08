from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import *


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'url', 'created_at', 'updated_at', 'bio', 'birth_date', 'city', 'country', 'clan', 'games',
            'gamertag', 'logo')

    def __init__(self, *args, **kwargs):
        super(ProfileSerializer, self).__init__(*args, **kwargs)
        
        self.fields["gamertag"].error_messages["required"] = u"gamertag is required"
        self.fields["gamertag"].error_messages["blank"] = u"gamertag cannot be blank"


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
