# from django.db import models
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=255)
    hospital_location = models.PointField(srid=32140, blank=True, null=True)
    hospital_address = models.CharField(max_length=400, null=True, blank=True)
    hospital_pin = models.IntegerField(null=True, blank=True)
    hospital_city = models.CharField(max_length=100, blank=True)
    hospital_state = models.CharField(max_length=100, blank=True)
    hospital_phone = PhoneNumberField(blank=True, null=True)
    hospital_about = models.TextField(max_length=2000, blank=True)
    hospital_rating = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.hospital_name
