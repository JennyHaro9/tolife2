from typing import Any

from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin


class TableView(SingleTableMixin, TemplateView):
    template_name = "base_templates/table_view.html"
    partial_template_name = "design_system/organisms/partial_table.html"
    table_class = None
    table_url = None
    section = ""
    title = ""
    table_pagination = {"per_page": 50}

    def get_template_names(self):
        return self.partial_template_name if self.request.htmx else self.template_name

    def get_table_kwargs(self):
        kwargs = super().get_table_kwargs()
        kwargs.update(hx_table_url=self.table_url)
        return kwargs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(section=self.section, title=self.title)
        return context
