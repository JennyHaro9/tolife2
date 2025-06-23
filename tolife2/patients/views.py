from typing import Any

from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django_tables2 import SingleTableMixin

from .tables import PatientTable


class PatientListView(SingleTableMixin, TemplateView):
    template_name = "patient/patient_list.html"
    partial_template_name = "design_system/organisms/partial_table.html"
    table_class = PatientTable
    table_url = reverse_lazy("patients:patient_list")
    section = "patients"

    def get_template_names(self):
        return self.partial_template_name if self.request.htmx else self.template_name

    def get_table_kwargs(self):
        kwargs = super().get_table_kwargs()
        kwargs.update(hx_table_url=self.table_url)
        return kwargs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(section=self.section)
        return context

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
