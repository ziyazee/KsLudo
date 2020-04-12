from django.db import models

# Create your models here.
class Ludo(models.Model):
    PlayerName=models.CharField(max_length=50)
    MatchesPlayed=models.IntegerField()
    TotalScore=models.IntegerField()
    Average=models.IntegerField()


class History(models.Model):
    First=models.CharField(max_length=50)
    Second=models.CharField(max_length=50)
    Third=models.CharField(max_length=50)
    Fourth=models.CharField(max_length=50)
