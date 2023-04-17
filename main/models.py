from django.db import models

# Create your models here.
class Ipl(models.Model):
    team_name = models.CharField(max_length=200, null=True, blank= True)
    wins = models.IntegerField(max_length=200, null=True, blank= True)
    losses = models.IntegerField(max_length=200, null=True, blank= True)
    played = models.IntegerField(max_length=200, null=True, blank= True)


    class Meta:
        db_table = 'IPL'