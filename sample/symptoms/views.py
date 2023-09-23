from django.shortcuts import render
from rest_framework.pagination import (LimitOffsetPagination, PageNumberPagination)
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from symptoms.serializers import SymptomsSerializer
from django.http.response import JsonResponse
from symptoms.models import Symptoms
from rest_framework.generics import ListAPIView
from sample.pagination import PostLimitOffsetPagination

# Create your views here.
@api_view(["POST", "GET"])
def symptoms(request):
    if request.method == "GET":
        paginator = PostLimitOffsetPagination()
        print("In get")
        query_set = Symptoms.objects.all()
        symptoms_name = request.GET.get('name', None)
        if symptoms_name is not None:
            query_set = query_set.filter(name=symptoms_name)
        print(query_set)
        result_page = paginator.paginate_queryset(query_set, request)
        symptoms_serializer = SymptomsSerializer(result_page, many=True)
        return JsonResponse(symptoms_serializer.data, safe=False)
    elif request.method == "POST":
        print("in post")
        symptoms_data = JSONParser().parse(request)
        print("symptoms data", symptoms_data)
        symptoms_serializer = SymptomsSerializer(data=symptoms_data)
        if symptoms_serializer.is_valid():
            symptoms_serializer.save()
            return JsonResponse(symptoms_serializer.data, status=201)
        return JsonResponse(symptoms_serializer.errors, status=400)

    class ApiSymptomsListView(ListAPIView):
        queryset = symptoms.objects.all()
        serializer_class = SymptomsSerializer

