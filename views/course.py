# course/views/organization_course.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView as _ListView,
    CreateView as _CreateView,
    UpdateView as _UpdateView,
    DeleteView as _DeleteView,
)
from ..models.course import Course
from ..tables.course import CourseTable
from ..forms.course import CourseForm


class ListView(_ListView):
    model = Course
    template_name = "course/list.html"
    table_class = CourseTable


class CreateView(_CreateView):
    model = Course
    form_class = CourseForm
    template_name = "course/form.html"
    success_url = reverse_lazy("courses:list")


class UpdateView(_UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "course/form.html"
    success_url = reverse_lazy("courses:list")


class DeleteView(_DeleteView):
    model = Course
    template_name = "course/delete.html"
    success_url = reverse_lazy("courses:list")
