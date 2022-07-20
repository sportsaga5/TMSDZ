from django.db import models

class Match(models.Model):
    first_team = models.CharField(max_length = 50)
    second_team = models.CharField(max_length = 50)
    description = models.TextField(blank=True, null=True)
    stadium = models.CharField(max_length = 50)
    start_date = models.DateTimeField()

    def __str__(self):
        return f'Match {self.pk}.  First team: {self.first_team}. Second team: {self.second_team}. Stadium: {self.stadium}'
