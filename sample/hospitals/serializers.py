from.models import Hospital
from rest_framework import serializers


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields=['hospital_id','hospital_name', 'hospital_location', 'hospital_address','hospital_rating','hospital_phone','hospital_pin','hospital_city','hospital_state', 'hospital_about']