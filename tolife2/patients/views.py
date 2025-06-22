import json
from datetime import timedelta

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django_tables2 import SingleTableView

from .models import ClinicalParameter
from .models import Patient
from .tables import PatientTable


class PatientListView(SingleTableView):
    model = Patient
    template_name = "patient/patient_list.html"
    table_class = PatientTable


patient_list_view = PatientListView.as_view()


def patient_detail_view(request, patient_id):  # noqa: C901
    patient = get_object_or_404(Patient, pk=patient_id)

    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    category = request.GET.get("category", "environment").lower()

    try:
        if start_date:
            start_date = timezone.now()
        if end_date:
            end_date = timezone.now()
    except ValueError:
        start_date = end_date = None

    if not start_date or not end_date:
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=7)

    clinical_data = ClinicalParameter.objects.filter(
        patient=patient,
        date__range=(start_date, end_date),
    ).order_by("date")

    categories = [
        "Environment",
        "Mic",
        "Sleep quality",
        "RF",
        "HR",
        "Mobility",
        "PPGWatch",
        "Spirometer",
        "CAT",
        "CCQ",
        "mMRC",
    ]

    def is_valid(cat):
        field = cat.lower().replace(" ", "")
        if field == "sleepquality":
            field = "sleep"
        if field == "ppgwatch":
            field = "ppg"
        if field == "mobility":
            field = "movility"
        if field == "spo2":
            field = "spo2"
        if field == "mmrc":
            return all(
                getattr(d, "index_validity_mMRC", False)
                and getattr(d, "data_validity_mMRC", False)
                for d in clinical_data
            )
        return all(
            getattr(d, f"index_validity_{field}", False)
            and getattr(d, f"data_validity_{field}", False)
            for d in clinical_data
        )

    show_graphs = is_valid(category)

    category_fields = {
        "environment": {
            "Temperatura día/noche": ["mean_temp_day", "mean_temp_night"],
            "Humedad día/noche": ["mean_hum_day", "mean_hum_night"],
            "Luminosidad día/noche": ["mean_lux_day", "mean_lux_night"],
            "Calidad del aire día/noche": ["mean_aqi_day", "mean_aqi_night"],
        },
        "mic": ["mean_si", "std_si", "min_si", "max_si"],
        "sleepquality": [
            "sleep_efficiency",
            "num_movements",
            "hours_bed",
            "total_movement",
        ],
        "rf": ["rf_mean", "rf_std", "rf_min", "rf_max"],
        "hr": ["hr_mean", "hr_std", "hr_min", "hr_max"],
        "mobility": [
            "gs_mean",
            "gs_std",
            "smwd_mean",
            "smwd_std",
            "sl_mean",
            "sl_std",
            "walked_time",
            "walked_distance",
        ],
        "ppgwatch": [
            "mean_hr",
            "range_hr_low",
            "range_hr_high",
            "std_rr",
            "range_stdrr_low",
            "range_stdrr_high",
            "rmssd",
            "range_rmssd_low",
            "range_rmssd_high",
        ],
        "spirometer": [
            "mean_fev1",
            "range_fev1_low",
            "range_fev1_high",
            "mean_pef",
            "range_pef_low",
            "spo2",
            "hr",
        ],
        "cat": ["cat"],
        "ccq": ["ccq"],
        "mmrc": ["mMRC"],
    }

    chart_data = []
    for d in clinical_data:
        entry = {"date": d.date.strftime("%Y-%m-%d")}
        fields = category_fields.get(category, [])
        if isinstance(fields, dict):
            for subgroup_fields in fields.values():
                for field in subgroup_fields:
                    entry[field] = getattr(d, field, None)
        else:
            for field in fields:
                entry[field] = getattr(d, field, None)
        chart_data.append(entry)

    context = {
        "patient": patient,
        "clinical_data": clinical_data,
        "categories": categories,
        "selected_category": category,
        "show_graphs": show_graphs,
        "start_date": start_date,
        "end_date": end_date,
        "category_fields": category_fields,
        "chart_data_json": json.dumps(chart_data, cls=DjangoJSONEncoder),
        "category_fields_json": json.dumps(category_fields, cls=DjangoJSONEncoder),
    }

    return render(request, "patients/patient_detail.html", context)
