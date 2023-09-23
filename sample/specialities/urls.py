from django.urls import path
from .views import SpecialistView

urlpatterns =[
    path('speciality',SpecialistView.as_view()),
]