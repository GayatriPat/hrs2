# from django.conf.urls import url
# from disease import views
#
# urlpatterns = [
#     url('disease', views.disease)
#
# ]
from django.urls import path
from .views import DiseaseDetail, DiseaseList, diseaseHospital, DiseaseView
urlpatterns =[
    # path('disease/',DiseaseList.as_view()),
    path('disease',DiseaseView.as_view()),
    # path('disease-get',DiseaseView.as_view()),
    # path('disease/<int:pk>/',DiseaseDetail.as_view()),
    # path('hospital-recommendation/', diseaseHospital)
]