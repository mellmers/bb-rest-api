from rest_framework import serializers
from .models import *


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name')


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    matches = MatchSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ('id', 'url', 'name', 'start_time', 'matches')
