from rest_framework import viewsets

from .models import Player
from .models import Woodcutting
from .serializers import PlayerSerializer
from .serializers import WoodcuttingSerializer


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.select_related(
        "woodcutting",
    ).all()
    serializer_class = PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.select_related(
        "woodcutting",
    ).all().filter(username="Dan")
    serializer_class = PlayerSerializer


class WoodcuttingViewSet(viewsets.ModelViewSet):
    queryset = Woodcutting.objects.all()
    serializer_class = WoodcuttingSerializer
