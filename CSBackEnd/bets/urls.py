from django.urls import path
from bets import views

urlpatterns = [
    path('all/', views.get_all_bets),
    path('', views.user_bets),
]