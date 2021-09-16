from django.db import models
from django.contrib.auth.models import User


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('games.Game', blank=True, null=True, on_delete=models.CASCADE)
    risk = models.IntegerField()
    day_placed = models.DateField()

