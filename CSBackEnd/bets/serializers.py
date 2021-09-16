from rest_framework import serializers
from .models import Bet

class BetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = ['id', 'user_id', 'game_id', 'risk', 'day_placed']