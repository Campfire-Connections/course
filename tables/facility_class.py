# course/tables/facility_class.py
"""
FacilityClassTable is a Django table that displays information about facility classes, including 
course details, enrollment, and timing.

This table is built using django-tables2 and is designed to present a structured view of the 
FacilityClass model, allowing for easy integration with Django views and templates.

Attributes:
    course: A column displaying the name of the associated course.
    facility_enrollment: A column displaying the name of the facility associated with the 
                        enrollment.
    start_time: A column displaying the start time of the facility class in a formatted manner.
    end_time: A column displaying the end time of the facility class in a formatted manner.
    max_enrollment: A column displaying the maximum capacity for the facility class.

    Meta:
        model: The model associated with this table, which is FacilityClass.
        fields: The fields to be included in the table representation.

    urls: A dictionary defining URL patterns for adding and editing facility classes.
    url_namespace: The namespace for the URLs related to facility classes.
"""

import django_tables2 as tables
from pages.tables.base import BaseTable

from ..models.facility_class import FacilityClass


class FacilityClassTable(BaseTable):
    """
    FacilityClassTable is a Django table that organizes and displays information about facility
    classes, including course names, facility details, and scheduling times.

    This table leverages django-tables2 to provide a structured representation of the FacilityClass
    model, facilitating easy integration with Django views and templates. It includes columns for
    course information, facility enrollment, start and end times, and maximum enrollment capacity.

    Attributes:
        course: A column that displays the name of the associated course.
        facility_enrollment: A column that displays the name of the facility linked to the
                            enrollment.
        start_time: A column that shows the start time of the facility class in a specified format.
        end_time: A column that shows the end time of the facility class in a specified format.
        max_enrollment: A column that indicates the maximum capacity for the facility class.

        Meta:
            model: The model associated with this table, which is FacilityClass.
            fields: The fields to be included in the table representation.

        urls: A dictionary defining URL patterns for adding and editing facility classes.
        url_namespace: The namespace for the URLs related to facility classes.
    """

    facility_enrollment = tables.Column(
        accessor="facility_enrollment.facility.name", verbose_name="Facility"
    )
    max_enrollment = tables.Column(verbose_name="Capacity")

    class Meta:
        model = FacilityClass
        fields = (
            "name",
            "facility_enrollment",
            "max_enrollment",
        )

    url_namespace = "facilities:classes"
    urls = {
        "add": {"kwargs": {"facility_slug": "facility_enrollment__facility__slug"}},
        "show": {
            "kwargs": {
                "facility_slug": "facility_enrollment__facility__slug",
                "facility_class_slug": "slug",
            }
        },
        "edit": {
            "kwargs": {
                "facility_slug": "facility_enrollment__facility__slug",
                "facility_class_slug": "slug",
            }
        },
        "delete": {
            "kwargs": {
                "facility_slug": "facility_enrollment__facility__slug",
                "facility_class_slug": "slug",
            }
        },
    }

    def getFacility(self, slug=False):
        facility = self.facility_enrollment.facility

        return facility.slug if slug else facility
