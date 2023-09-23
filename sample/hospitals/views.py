from disease.models import Disease
from sample import settings
from specialities.models import Speciality
from doctors.models import Doctor
from .serializers import HospitalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from rest_framework import status
from disease import serializers as diseaseSerializer
from specialities import serializers as specialitySerializer
from doctors import serializers as doctorSerializer
from hospitals import serializers as hospitalSerializer
from django.contrib.gis.db.models.functions import Distance
from.models import Hospital
import json

class HospitalListView(APIView):
    def get_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipAddress = x_forwarded_for.split(',')[0]
        else:
            ipAddress = request.META.get('REMOTE_ADDR')

        print("ip address is ====", ipAddress)
        return ipAddress

    def post(self, request):
        hospitalData = request.data
        print("doctor data", hospitalData)
        serializer = HospitalSerializer(data=hospitalData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        predictedDisease = request.GET.get('disease', None)
        print("disease is", predictedDisease)

        disease_data = Disease.objects.get(disease_name=predictedDisease)
        serializer = diseaseSerializer.DiseaseSerializer(disease_data)
        speciality_id = serializer.data.get('disease_speciality')

        speciality_data = Speciality.objects.get(speciality_id=speciality_id)
        speciality_serializer = specialitySerializer.SpecialitySerializer(speciality_data)
        speciality_name = speciality_serializer.data.get('speciality_name')

        doctor_data = Doctor.objects.filter(doctor_speciality=speciality_name)
        print("doctor data is", doctor_data);
        doctor_serializer = doctorSerializer.DoctorSerializer(doctor_data, many=True)
        print("doctor serialize data", doctor_serializer.data);

        hospital_id_list = []
        for data in doctor_serializer.data:
            modified_data = dict(data)
            hospital_id_list.append(modified_data.get('doctor_hospital'))
            print("hospital is", hospital_id_list)

        if hospital_id_list:
            ref_location = Point(12853611.01702177, 14479612.3328968, srid=32140)
            pnt = GEOSGeometry(settings.ipAddresss, srid=32140) # question
            hospitals_data = Hospital.objects.filter(hospital_id__in=hospital_id_list, hospital_location__distance_lte=(pnt, 15000)).annotate(distance=Distance("hospital_location", ref_location)).order_by('distance')
            hospital_serializer = hospitalSerializer.HospitalSerializer(hospitals_data, many=True)
            # hospital_list.append(hospital_serializer.data)
            # for hospital in hospital_serializer.data:
            #     modified_data = dict(hospital)
            #     hospital_point = modified_data.get('hospital_location')
            #     print(GEOSGeometry(hospital_point))
            #     pnt1 = Point(12853611.01702177, 14479612.3328968)     #question
            #     pnt2 = Point(12848744.28903654, 14479244. 73548545)
            #     distance = pnt1.distance(pnt2)
            #     print("distance is=====================", distance)
            #     print("hospital location is", modified_data.get('hospital_location'))

            return Response(hospital_serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

class HospitalView(APIView):
        def get_object(self, id):
            try:
                return Hospital.objects.get(hospital_id=id)
            except Hospital.DoesNotExist:
                return None

        def get(self, request, id):
            doctorData = Doctor.objects.filter(doctor_hospital_id=id);
            doctor_Serializer = doctorSerializer.DoctorSerializer(doctorData, many=True);
            hospital_instance = self.get_object(id)
            if not hospital_instance:
                return Response(
                    {"res": "Object with todo id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = hospitalSerializer.HospitalSerializer(hospital_instance)
            doctorsList = json.dumps({"doctors_list": doctor_Serializer.data})
            hospitalData = json.dumps(serializer.data)
            dictA = json.loads(hospitalData)
            dictB = json.loads(doctorsList)
            dictA.update(dictB)
            jsonStrinA = json.dumps(dictA)
            print(jsonStrinA)
            return Response(json.loads(jsonStrinA), status=status.HTTP_200_OK)
