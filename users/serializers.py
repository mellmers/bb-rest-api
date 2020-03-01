from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'groups')

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

        # self.fields["gamertag"].error_messages["required"] = u"gamertag is required"
        # self.fields["gamertag"].error_messages["blank"] = u"gamertag cannot be blank"
