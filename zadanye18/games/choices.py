from django.db import models


class GameType(models.TextChoices):
    STANDART = 'ST'
    PREMIUM = 'PR'
