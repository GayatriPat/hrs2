from django.contrib import admin
from.models import Doctor

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_id','doctor_name','doctor_hospital']
admin.site.register(Doctor, DoctorAdmin)