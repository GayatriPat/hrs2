from django.contrib import admin
from django.contrib.gis import admin
from .models import Hospital
# Register your models here.
class HospitalAdmin(admin.OSMGeoAdmin):
    list_display = ['hospital_id','hospital_name','hospital_location','hospital_address','hospital_rating']
admin.site.register(Hospital, HospitalAdmin)