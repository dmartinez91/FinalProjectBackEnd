from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_One_Name = models.CharField(max_length=50)
    team_Two_Name = models.CharField(max_length=50)
    team_One_Spread = models.IntegerField()
    team_Two_Spread = models.IntegerField()
    team_One_ML = models.IntegerField()
    team_Two_ML = models.IntegerField()
    over_under = models.IntegerField()
    gameDay = models.DateField()