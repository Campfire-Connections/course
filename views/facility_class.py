# course/views/facility_class.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView as _ListView,
    DetailView as _DetailView,
    CreateView as _CreateView,
    UpdateView as _UpdateView,
    DeleteView as _DeleteView,
)

from ..models.facility_class import FacilityClass

class ListView(_ListView):
    model = FacilityClass
    template_name = "facility-class/index.html"
    context_object_name = "facility_classes"


class ShowView(_DetailView):
    model = FacilityClass
    template_name = "facility-class/show.html"
    context_object_name = "facility_class"


class CreateView(_CreateView):
    model = FacilityClass
    fields = "__all__"
    template_name = "facility-class/form.html"
    success_url = reverse_lazy("facilities:classes:index")


class UpdateView(_UpdateView):
    model = FacilityClass
    fields = "__all__"
    template_name = "facility-class/form.html"
    success_url = reverse_lazy("courses:facility-classes:index")


class DeleteView(_DeleteView):
    model = FacilityClass
    template_name = "facility-class/confirm_delete.html"
    success_url = reverse_lazy("courses:facility-classes:index")
