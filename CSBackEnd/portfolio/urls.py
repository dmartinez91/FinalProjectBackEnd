from django.urls import path
from portfolio import views

urlpatterns = [
    path('all/', views.get_all_portoflios),
    path('', views.user_Portfolio)
]