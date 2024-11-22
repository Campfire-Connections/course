# course/tables/requirement.py

import django_tables2 as tables
from ..models.requirement import Requirement

class RequirementTable(tables.Table):
    name = tables.Column(verbose_name="Requirement Name")
    description = tables.Column(verbose_name="Description")
    course = tables.Column(verbose_name="Course")

    class Meta:
        model = Requirement
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "description", "course")
        attrs = {"class": "table table-striped table-bordered"}
