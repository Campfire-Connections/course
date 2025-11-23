# course/views/requirement.py

from django.urls import reverse_lazy

from core.views.base import (
    BaseTableListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
)

from ..models.requirement import Requirement
from ..tables.requirement import RequirementTable
from ..forms.requirement import RequirementForm


class ListView(BaseTableListView):
    model = Requirement
    template_name = "requirement/list.html"
    table_class = RequirementTable
    context_object_name = "requirements"


class CreateView(BaseCreateView):
    model = Requirement
    form_class = RequirementForm
    template_name = "requirement/form.html"
    success_url = reverse_lazy("courses:requirements:list")


class UpdateView(BaseUpdateView):
    model = Requirement
    form_class = RequirementForm
    template_name = "requirement/form.html"
    success_url = reverse_lazy("courses:requirements:list")


class DeleteView(BaseDeleteView):
    model = Requirement
    template_name = "requirement/confirm_delete.html"
    success_url = reverse_lazy("courses:requirements:list")
