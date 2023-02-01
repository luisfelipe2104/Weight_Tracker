from django.db import models

# Create your models here.
class Weight(models.Model):
    weight = models.IntegerField()
    date = models.DateField()