from django.shortcuts import render
from.models import Speciality
from.serializers import SpecialitySerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import generics

# class SpecialityList(generics.ListCreateAPIView):
#     queryset = Speciality.objects.all()
#     serializer_class = SpecialitySerializer
#
# class SpecialityDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Speciality.objects.all()
#     serializer_class = SpecialitySerializer

class SpecialistView(GenericAPIView):

    def post(self, request):
        specialistData = request.data
        serializer = SpecialitySerializer(data=specialistData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("errors are", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
