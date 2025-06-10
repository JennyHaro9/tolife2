from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import ClinicalMeasurement
from .models import Doctor
from .models import Patient


@login_required
def patient_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    patients = Patient.objects.filter(doctor=doctor)
    return render(request, "clinical/patient_list.html", {"patients": patients})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk, doctor__user=request.user)
    measurements = ClinicalMeasurement.objects.filter(patient=patient).select_related(
        "parameter",
    )
    variables = [
        {
            "variable_name": m.parameter.name_parameter,
            "value": m.value,
            "unit": m.parameter.units,
            "date_recorded": m.timestamp,
        }
        for m in measurements
    ]
    context = {
        "patient": patient,
        "variables": variables,
    }
    return render(request, "clinical/patient_detail.html", context)
