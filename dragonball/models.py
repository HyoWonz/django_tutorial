from django.db import models

# Create your models here.
class Dragonball(models.Model):
    dragonball=models.CharField(max_length=5)
    detected=models.CharField(max_length=10)