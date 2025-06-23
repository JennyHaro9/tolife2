import django_tables2 as tables
from django_tables2.utils import A


class PatientTable(tables.Table):
    name = tables.Column()
    identifier = tables.LinkColumn("patients:patient_detail", args=[A("id")])
    doctor = tables.Column()

    class Meta:
        fields = ("name", "identifier", "doctor")
        template_name = "design_system/organisms/bootstrap_responsive_table.html"
