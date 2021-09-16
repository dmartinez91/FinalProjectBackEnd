from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    home_Team = models.CharField(max_length=50)
    away_Team = models.CharField(max_length=50)
    home_Team_Spread = models.FloatField()
    away_Team_Spread = models.FloatField()
    home_Team_ML = models.IntegerField()
    away_Team_ML = models.IntegerField()
    over_under = models.IntegerField()
    gameDay = models.DateField()
    sports_Book = models.CharField(max_length=50)