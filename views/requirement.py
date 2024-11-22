# course/views/requirement.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView as _ListView,
    CreateView as _CreateView,
    UpdateView as _UpdateView,
    DeleteView as _DeleteView,
)
from ..models.requirement import Requirement
from ..tables.requirement import RequirementTable
from ..forms.requirement import RequirementForm

class ListView(_ListView):
    model = Requirement
    template_name = 'requirement/list.html'
    table_class = RequirementTable

class CreateView(_CreateView):
    model = Requirement
    form_class = RequirementForm
    template_name = 'requirement/form.html'
    success_url = reverse_lazy('courses:requirements:list')

class UpdateView(_UpdateView):
    model = Requirement
    form_class = RequirementForm
    template_name = 'requirement/form.html'
    success_url = reverse_lazy('courses:requirements:list')

class DeleteView(_DeleteView):
    model = Requirement
    template_name = 'requirement/confirm_delete.html'
    success_url = reverse_lazy('courses:requirements:list')
