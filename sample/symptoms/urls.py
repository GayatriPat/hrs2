from django.conf.urls import url
from symptoms import views

urlpatterns = [
    url('api/symptoms', views.symptoms)
]
