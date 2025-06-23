from django.urls import path

from .views import patient_detail_view
from .views import patient_list_view

app_name = "patients"

urlpatterns = [
    path("", patient_list_view, name="patient_list"),
    path("<pk>/", patient_detail_view, name="patient_detail"),
]
