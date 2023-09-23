
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('', include('symptoms.urls')),
    # path('', include('disease.urls')),
    path('api/',include('specialities.urls')),
    path('api/',include('hospitals.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('disease.urls')),
]
