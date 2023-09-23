from django.urls import path
from .views import DoctorDetail, DoctorList, DoctorView
urlpatterns =[
    path('doctor/',DoctorList.as_view()),
    path('doctor-save',DoctorView.as_view()),
    path('doctor/<int:pk>/',DoctorDetail.as_view()),
]