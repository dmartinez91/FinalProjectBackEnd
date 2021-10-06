from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Portfolio
from .serializers import PortfolioSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_portoflios(request):
    portfolio = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolio, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_Portfolio(request):

    print('User', f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        portfolio = Portfolio.objects.filter(user_id=request.user.id)
        serializer = PortfolioSerializer(portfolio, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        portfolio = Portfolio.objects.all().delete()
        return Response({'DELETED'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['DELETE'])
# def portfolio_delete(request, pk):
#     try: 
#         linkedPortfolio = Portfolio.objects.get(pk=pk) 
#     except Portfolio.DoesNotExist:
#         return Response({'something is happening'}, status=status.HTTP_404_NOT_FOUND) 
#     if request.method == 'DELETE':
#         linkedPortfolio.delete() 
#         return Response({'message': 'Portfolio was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)