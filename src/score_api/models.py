from django.db import models



class Game(models.Model):
    name = models.CharField(max_length=200)


class Score(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    player = models.CharField(max_length=200)
    score = models.FloatField()