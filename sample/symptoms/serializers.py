from rest_framework import serializers
from symptoms.models import Symptoms

class SymptomsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptoms
        fields = ('name',)
