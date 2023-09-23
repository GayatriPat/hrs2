from django.contrib import admin
from .models import Symptoms
# Register your models here.
@admin.register(Symptoms)
class SymptomAdmin(admin.ModelAdmin):
    list_display=['name',]