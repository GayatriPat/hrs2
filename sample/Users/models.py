from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.TextField(max_length=60, blank=False)
    email = models.EmailField()
    password = models.TextField(max_length=12)
