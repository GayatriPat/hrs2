from django.db import models
from specialities.models import Speciality

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255, unique=True)
    disease_description = models.CharField(max_length=1000, null=True,blank=True)
    disease_precaution1 = models.CharField(max_length=100, null=True,blank=True)
    disease_precaution2 = models.CharField(max_length=100, null=True,blank=True)
    disease_precaution3 = models.CharField(max_length=100, null=True,blank=True)
    disease_precaution4 = models.CharField(max_length=100, null=True,blank=True)
    disease_speciality = models.ForeignKey(Speciality,to_field='speciality_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.disease_name