from django.urls import path
from portfolio import views

urlpatterns = [
    path('all/', views.get_all_portoflios),
    path('', views.user_Portfolio),
    path('<int:pk>', views.portfolio_delete_update)
]