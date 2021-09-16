from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'sports_Book', 'home_Team', 'away_Team', 'home_Team_Spread', 'away_Team_Spread', 'home_Team_ML', 'away_Team_ML', 'over_under', 'gameDay', 'user_id']

