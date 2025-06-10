from django.contrib import admin

from .models import ClinicalMeasurement
from .models import ClinicalParameter
from .models import Doctor
from .models import Patient

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(ClinicalParameter)
admin.site.register(ClinicalMeasurement)
