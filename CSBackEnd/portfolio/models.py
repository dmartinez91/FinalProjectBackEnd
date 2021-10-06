from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    betsWon = models.IntegerField()
    betLost = models.IntegerField()
    moneyWon = models.IntegerField()
    moneyLost = models.IntegerField()
    netGain = models.IntegerField()

