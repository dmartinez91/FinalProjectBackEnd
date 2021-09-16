from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'team_One_Name', 'team_Two_Name', 'team_One_Spread', 'team_Two_Spread', 'team_One_ML', 'team_Two_ML', 'over_under', 'gameDay', 'user_id']
