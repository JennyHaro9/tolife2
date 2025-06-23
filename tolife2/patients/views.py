from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from tolife2.utils.views import TableView

from .tables import PatientTable


class PatientListView(TableView):
    table_class = PatientTable
    table_url = reverse_lazy("patients:patient_list")
    section = "patients"
    title = "Patients"

    def get_table_data(self):
        return [
            {
                "id": 1,
                "name": "Lucía Gómez",
                "identifier": "P001",
                "doctor": "Dra. Ana Martínez",
            },
            {
                "id": 2,
                "name": "Carlos Ramírez",
                "identifier": "P002",
                "doctor": "Dr. Luis Fernández",
            },
            {
                "id": 3,
                "name": "Elena Torres",
                "identifier": "P003",
                "doctor": "Dr. Miguel Álvarez",
            },
            {
                "id": 4,
                "name": "Jorge Herrera",
                "identifier": "P004",
                "doctor": "Dra. Ana Martínez",
            },
            {
                "id": 5,
                "name": "Marta Castillo",
                "identifier": "P005",
                "doctor": "Dr. Luis Fernández",
            },
        ]


patient_list_view = PatientListView.as_view()


class PatientDetailView(TemplateView):
    template_name = "patient/patient_detail.html"


patient_detail_view = PatientDetailView.as_view()
