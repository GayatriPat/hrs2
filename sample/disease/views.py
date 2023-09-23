from django.core import paginator
from django.http import JsonResponse
from django.shortcuts import render
from doctors.models import Doctor

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from disease import getDisease
from disease.models import Disease
from disease.serializers import DiseaseSerializer
from symptoms.serializers import SymptomsSerializer

@api_view([ "GET"])
def diseaseHospital(request):
    if request.method == "GET":
        print("in get")
        symptoms_name = request.GET.get('symptoms', None)
        print(symptoms_name)
        predictedDisease=getDisease.predictDisease(symptoms_name)
        print("Predicted disease", predictedDisease)

        l = []
        disease = Disease.objects.get(disease_name=predictedDisease)
        speciality = disease.disease_speciality.speciality_id
        doctors = Doctor.objects.filter(doctor_speciality=speciality)
        for doctor in doctors:
            l.append(doctor.doctor_hospital.hospital_name)
            print(doctor.doctor_hospital.hospital_name)

    # return JsonResponse({"message": predictedDisease}, status=200)
        return JsonResponse({"message": l}, status=200)

   # class ApiDiseaseListView(ListAPIView):
    #    queryset = disease.objects.all()
     #   serializer_class = SymptomsSerializer

class DiseaseList(generics.ListCreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseView(GenericAPIView):

    def post(self, request):
        diseaseData = request.data
        serializer = DiseaseSerializer(data=diseaseData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        symptoms_name = request.GET.get('symptoms', None)
        print("symptoms name", symptoms_name)
        predictedDisease = getDisease.predictDisease(symptoms_name)

        return Response({'disease_name': predictedDisease}, status=status.HTTP_200_OK)
