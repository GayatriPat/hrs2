from django.db import models

# Create your models here.
class Speciality(models.Model):
    speciality_id = models.AutoField(primary_key=True)
    speciality_name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return self.speciality_name