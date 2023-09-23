from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['doctor_id','doctor_name','doctor_hospital','doctor_speciality','year_of_experience', 'doctor_degree']