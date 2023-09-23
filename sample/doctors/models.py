from django.db import models
from specialities.models import Speciality
from hospitals.models import Hospital

class Doctor(models.Model):
    MBBS = "MBBS"
    MS = "MS"
    MD = "MD"
    BAMS = "BAMS"
    BHMS = "BHMS"

    degree_choices = (
        (MBBS, MBBS),
        (MS, MS),
        (MD, MD),
        (BAMS, BAMS),
        (BHMS, BHMS)
    )
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=255)
    doctor_speciality = models.ForeignKey(Speciality, to_field='speciality_name', on_delete=models.CASCADE)
    doctor_hospital = models.ForeignKey(Hospital,null=True,on_delete=models.CASCADE)
    doctor_degree = models.CharField(max_length=255, choices=degree_choices, null=True)
    year_of_experience = models.FloatField(max_length=50,null=True)
    def __str__(self):
        return self.doctor_name
