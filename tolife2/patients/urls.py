from django.urls import path

from .views import patient_list_view

app_name = "patients"

urlpatterns = [
    path("", patient_list_view, name="patient_list"),
]
