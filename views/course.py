# course/views/organization_course.py

from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from core.views.base import (
    BaseIndexByFilterTableView,
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseTableListView,
    BaseUpdateView,
)

from ..models.course import Course
from ..tables.course import CourseTable
from ..forms.course import CourseForm


class IndexView(BaseTableListView):
    model = Course
    template_name = "course/list.html"
    table_class = CourseTable
    context_object_name = "courses"


class CreateView(BaseCreateView):
    model = Course
    form_class = CourseForm
    template_name = "course/form.html"
    success_url = reverse_lazy("courses:list")


class UpdateView(BaseUpdateView):
    model = Course
    form_class = CourseForm
    template_name = "course/form.html"
    success_url = reverse_lazy("courses:list")


class DeleteView(BaseDeleteView):
    model = Course
    template_name = "course/delete.html"
    success_url = reverse_lazy("courses:list")

class ShowView(BaseDetailView):
    model = Course
    template_name = "course/show.html"
    context_object_name = "course"
    slug_field = "slug"
    slug_url_kwarg = "course_slug"

    def get_object(self):
        course_id = self.kwargs.get("course_id")
        course_slug = self.kwargs.get("course_slug")
        if course_id:
            return get_object_or_404(Course, pk=course_id)
        else:
            return get_object_or_404(Course, slug=course_slug)

