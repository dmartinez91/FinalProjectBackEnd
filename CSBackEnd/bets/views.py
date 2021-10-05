from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Bet
from .serializers import BetSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_bets(request):
    bets = Bet.objects.all()
    serializer = BetSerializer(bets, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_bets(request):
    if request.method == 'POST':
        try:
            user_id= request.user.id
            game_id= request.data.get('game_id')
            risk= request.data.get('risk')
            day_placed = request.data.get('day_placed')
            oddspicked = request.data.get('oddspicked')
            newBet = Bet(user_id=user_id, game_id=game_id,risk=risk,day_placed=day_placed, oddspicked=oddspicked)
            newBet.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'GET':
        bets = Bet.objects.filter(user_id=request.user.id)
        serializer =BetSerializer(bets, many=True)
        return Response(serializer.data)



# code that i had before using serializer, would allow me to post a bet, but would not link the game_id to the game, would
# return null value and then i would have to manually change it as an admin 
# def user_bets(request):
#     if request.method == 'POST':
#         serializer = BetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
