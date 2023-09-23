import json

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from Users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from sample import settings
from django.contrib.auth import authenticate
import jwt


# Create your views here.
# @api_view(['GET', 'POST'])
# def register(request):
#     if request.method == "GET":
#         print(request.query_params)
#     elif request.method == "POST":
#         userData = JSONParser().parse(request)
#         userSerializerData = UserSerializer(data=userData)
#
#         print("req data is ", userData)
#         print("serializer data is", userSerializerData)
#         if userSerializerData.is_valid():
#             print("is it coming here")
#             userSerializerData.save()
#             print("user serializer", userSerializerData)
#             return JsonResponse(userSerializerData.data, status=200, safe=False)
#     return JsonResponse({'message': 'Done'})
#
# @api_view(['POST'])
# def logIn(request):
#     if request.method == "POST":
#         userData = JSONParser().parse(request)

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        # userData = json.dumps(request.data)
        userData = request.data
        print("my data", userData)
        serializer = UserSerializer(data=userData)
        if serializer.is_valid():
            print("is it valid ")
            serializer.save()
            return Response(serializer.data)
        print("errors are", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LogIn
class LoginView(GenericAPIView):

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)

        print("user is", user)
        if user:
            auth_token = jwt.encode({'email': user.email}, settings.JWT_SECRET_KEY, algorithm="HS256")
            serializer = UserSerializer(user)
            data = {
                'user': serializer.data,
                'token': auth_token
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)