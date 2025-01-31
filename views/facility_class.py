# course/views/facility_class.py

from django.urls import reverse_lazy

from core.views.base import (
    BaseIndexByFilterTableView,
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseTableListView,
    BaseUpdateView,
)

from ..models.facility_class import FacilityClass
from ..tables.facility_class import FacilityClassTable


class ListView(BaseTableListView):
    model = FacilityClass
    template_name = "facility-class/list.html"
    context_object_name = "facility_classes"
    table_class = FacilityClassTable


class ShowView(BaseDetailView):
    model = FacilityClass
    template_name = "facility-class/show.html"
    context_object_name = "facility_class"


class CreateView(BaseCreateView):
    model = FacilityClass
    fields = "__all__"
    template_name = "facility-class/form.html"
    success_url = reverse_lazy("facilities:classes:index")


class UpdateView(BaseUpdateView):
    model = FacilityClass
    fields = "__all__"
    template_name = "facility-class/form.html"
    success_url = reverse_lazy("courses:facility-classes:index")


class DeleteView(BaseDeleteView):
    model = FacilityClass
    template_name = "facility-class/confirm_delete.html"
    success_url = reverse_lazy("courses:facility-classes:index")
