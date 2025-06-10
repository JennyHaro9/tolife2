from django.contrib import admin
from .models import Doctor, Patient, ClinicalParameter, ClinicalMeasurement

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(ClinicalParameter)
admin.site.register(ClinicalMeasurement)
