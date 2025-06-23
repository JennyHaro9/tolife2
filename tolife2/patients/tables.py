import django_tables2 as tables


class PatientTable(tables.Table):
    name = tables.Column(verbose_name="Name")
    identifier = tables.Column(verbose_name="Identifier")
    doctor = tables.Column(verbose_name="Doctor")
    actions = tables.TemplateColumn(
        verbose_name="",
        extra_context={"patient_detail_url": "patients:patient_detail"},
        template_code="""
    <button
  class="btn btn-outline-primary"
  hx-get="{% url patient_detail_url record.id %}"
  hx-target="#table-wrapper"
  hx-swap="innerHTML"
  title="Mostrar gráfica de parámetros"
>
  <i class="bi bi-bar-chart-fill"></i>
</button>
    """,
    )

    def __init__(self, **kwargs):
        self.hx_table_url = kwargs.pop("hx_table_url")
        super().__init__(**kwargs)

    class Meta:
        fields = ("name", "identifier", "doctor")
        template_name = "design_system/organisms/bootstrap_responsive_table.html"
