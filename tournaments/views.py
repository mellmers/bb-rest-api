from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class TournamentView(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class MatchView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
