from django.urls import path
from rest_framework import views
from games import views

urlpatterns = [
    path('all/', views.get_all_games),
    path('', views.user_games),
]