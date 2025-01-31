# course/tables/course.py
"""
CourseTable is a Django table that organizes and displays information about courses, including 
their names, descriptions, images, and active status.

This table is built using django-tables2 and provides a structured view of the Course model. It 
includes columns for course name, description, image representation, and the active status of the 
course. The `render_active` method formats the active status into a visually distinct badge, 
indicating whether the course is active or inactive.

Attributes:
    name: A column that displays the name of the course.
    description: A column that displays a brief description of the course.
    image: A column that displays an image associated with the course.
    active: A column that indicates whether the course is currently active.

    Meta:
        model: The model associated with this table, which is Course.
        fields: The fields to be included in the table representation.

Methods:
    render_active(value):
        Formats the active status into a badge with appropriate styling.

Args:
    value: A boolean indicating the active status of the course.

Returns:
    A safe HTML string representing the active status as a badge.
"""

import django_tables2 as tables
from django.utils.safestring import mark_safe
from core.tables.base import BaseTable

from ..models.course import Course


class CourseTable(BaseTable):
    """
    CourseTable is a Django table that organizes and displays information about courses, including
    their names, descriptions, images, and active status.

    This table is built using django-tables2 and provides a structured view of the Course model. It
    includes columns for course name, description, image representation, and the active status of
    the course. The `render_active` method formats the active status into a visually distinct badge,
    indicating whether the course is active or inactive.

    Attributes:
        name: A column that displays the name of the course.
        description: A column that displays a brief description of the course.
        image: A column that displays an image associated with the course.
        active: A column that indicates whether the course is currently active.

        Meta:
            model: The model associated with this table, which is Course.
            fields: The fields to be included in the table representation.

    Methods:
        render_active(value):
            Formats the active status into a badge with appropriate styling.

    Args:
        value: A boolean indicating the active status of the course.

    Returns:
        A safe HTML string representing the active status as a badge.
    """

    name = tables.Column(verbose_name="Course Name")
    description = tables.Column(verbose_name="Description")
    image = tables.Column(verbose_name="Image")
    active = tables.Column(verbose_name="Status")

    class Meta:
        model = Course
        fields = ("name", "description", "image", "active")

    def render_active(self, value):
        status_label = "Active" if value else "Inactive"
        css_class = "badge-success" if value else "badge-secondary"
        return mark_safe(f'<span class="badge {css_class}">{status_label}</span>')

    url_namespace = "courses"
    urls = {
        "add": {"kwargs": {"facility_slug": "facility__slug"}},
        "show": {"kwargs": {"course_slug": "slug"}},
        "edit": {"kwargs": {"course_slug": "slug"}},
        "delete": {"kwargs": {"course_slug": "slug"}},
    }
    available_actions = ["show", "edit", "delete"]
