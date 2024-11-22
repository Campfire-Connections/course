# course/models/facility_class.py

from django.db import models
from django.core.exceptions import ValidationError

from pages.mixins import models as mixins
from pages.mixins import settings as stgs
from enrollment.models.organization import OrganizationCourse
from enrollment.models.facility import FacilityEnrollment


class FacilityClass(
    mixins.NameDescriptionMixin,
    mixins.TimestampMixin,
    mixins.SoftDeleteMixin,
    mixins.AuditMixin,
    mixins.SlugMixin,
    mixins.ActiveMixin,
    stgs.SettingsMixin,
    models.Model,
):
    """Facility Class Model."""

    organization_course = models.ForeignKey(
        OrganizationCourse,
        on_delete=models.CASCADE,
        related_name="facility_classes",
        verbose_name="Organization Course",
    )
    facility_enrollment = models.ForeignKey(
        FacilityEnrollment,
        on_delete=models.CASCADE,
        related_name="facility_classes",
        verbose_name="Facility Enrollment",
    )
    max_enrollment = models.PositiveIntegerField(default=30)  # New field

    def clean(self):
        """Ensure class is within the enrollment period of the facility."""
        if self.max_enrollment < 1:
            raise ValidationError("Maximum enrollment must be at least 1.")
        super().clean()

    class Meta:
        """Metadata."""

        verbose_name = "Facility Class"
        verbose_name_plural = "Facility Classes"
        ordering = ["name"]
        indexes = [models.Index(fields=["slug", "name"])]

    def __str__(self):
        """String representation."""

        course = self.organization_course.course.name
        facility = self.facility_enrollment.facility.name

        return f"{self.name} ({course} at {facility})"
