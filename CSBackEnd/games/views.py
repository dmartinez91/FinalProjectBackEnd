from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Game
from .serializers import GameSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_games(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_games(request):

    print('User', f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        games = Game.objects.filter(user_id=request.user.id)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
