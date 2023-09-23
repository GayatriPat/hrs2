from django.urls import path
from .views import (HospitalListView, HospitalView)

urlpatterns =[
    # path('hospital/',HospitalList.as_view()),
    path('hospital-save', HospitalListView.as_view()),
    path('hospital/<int:id>',HospitalView.as_view()),
]