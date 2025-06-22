from django.urls import path

from . import views

urlpatterns = [
    path("", views.patients_list, name="home"),  # será /pacientes/
    path(
        "<int:patient_id>/",
        views.patient_detail_view,
        name="patient_detail",
    ),  # será /pacientes/1/
]
