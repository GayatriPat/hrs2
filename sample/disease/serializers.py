from.models import Disease
from rest_framework import serializers


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fields=['disease_id','disease_name','disease_description','disease_precaution1','disease_precaution2','disease_precaution3','disease_precaution4','disease_speciality']
