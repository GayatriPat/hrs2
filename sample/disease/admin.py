from django.contrib import admin
from.models import Disease
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['disease_id','disease_name','disease_description','disease_precaution1','disease_precaution2','disease_precaution3','disease_precaution4','disease_speciality']
admin.site.register(Disease, DiseaseAdmin)