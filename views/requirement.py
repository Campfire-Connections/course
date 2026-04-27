# course/views/requirement.py

from django.urls import reverse_lazy

from core.views.base import (
    BaseTableListView,
    BaseDetailView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
)

from ..models.requirement import Requirement
from ..tables.requirement import RequirementTable
from ..forms.requirement import RequirementForm
from ..selectors import requirement_detail_queryset, requirement_list_queryset


class ListView(BaseTableListView):
    model = Requirement
    template_name = "requirement/list.html"
    table_class = RequirementTable
    context_object_name = "requirements"

    def get_queryset(self):
        return requirement_list_queryset()


class CreateView(BaseCreateView):
    model = Requirement
    form_class = RequirementForm
    template_name = "requirement/form.html"
    success_url = reverse_lazy("requirements:index")


class ShowView(BaseDetailView):
    model = Requirement
    template_name = "base/show.html"
    context_object_name = "requirement"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return requirement_detail_queryset()


class UpdateView(BaseUpdateView):
    model = Requirement
    form_class = RequirementForm
    template_name = "requirement/form.html"
    success_url = reverse_lazy("requirements:index")


class DeleteView(BaseDeleteView):
    model = Requirement
    template_name = "requirement/confirm_delete.html"
    success_url = reverse_lazy("requirements:index")
