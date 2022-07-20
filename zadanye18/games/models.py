from django.db import models
from .choices import GameType

# Create your models here.

class Game(models.Model):
    deposit = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    game_type = models.CharField(max_length=2, choices=GameType.choices, default=GameType.STANDART)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Game {self.pk}. Game type: {self.game_type}. Deposit: {self.deposit}'
