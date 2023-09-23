from .models import Speciality
from rest_framework import serializers

class  SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Speciality
        fields=['speciality_id','speciality_name',]
