from django.urls import path
from bets import views

urlpatterns = [
    path('all/', views.get_all_bets),
    path('', views.user_bets),
    path('<int:pk>', views.delete_betslip)
]