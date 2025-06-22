import django_tables2 as tables

from tolife2.patients.models import Patient


class PatientTable(tables.Table):
    class Meta:
        model = Patient
        fields = ("name", "identifier", "doctor")
