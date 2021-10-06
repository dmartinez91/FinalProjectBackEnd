from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'betsWon', 'betLost', 'moneyWon', 'moneyLost', 'netGain', 'user_id']