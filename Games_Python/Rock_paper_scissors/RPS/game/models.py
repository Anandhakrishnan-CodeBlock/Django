from django.contrib.auth.models import User
from django.db import models


class Score(models.Model):
    no_game_payed = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    sample = models.CharField(max_length=100, default='')
