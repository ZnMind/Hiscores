from __future__ import annotations

from rest_framework import serializers

from .models import Player, Woodcutting


class WoodcuttingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woodcutting
        fields = ["level", "experience", "experience_next"]


class PlayerSerializer(serializers.ModelSerializer):
    woodcutting = WoodcuttingSerializer()

    class Meta:
        model = Player
        fields = "__all__"
        lookup_field = "username"

    def create(self, validated_data):
        woodcutting_data = validated_data.pop('woodcutting')
        player = Player.objects.create(**validated_data)
        Woodcutting.objects.create(player=player, **woodcutting_data)
        return player
