from django.contrib import admin
from.models import Speciality
# Register your models here.
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['speciality_id','speciality_name',]
admin.site.register(Speciality, SpecialityAdmin)