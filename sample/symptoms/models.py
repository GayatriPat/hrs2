from django.db import models


# Create your models here.
class Symptoms(models.Model):
    name = models.CharField(max_length=100)
