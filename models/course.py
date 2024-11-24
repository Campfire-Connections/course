# course/models/course.py

from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

from taggit.managers import TaggableManager

from core.mixins import models as mixins
from core.mixins import settings as stgs
from enrollment.models.organization import OrganizationEnrollment, OrganizationCourse

from .requirement import Requirement

class Course(
    mixins.NameDescriptionMixin,
    mixins.TimestampMixin,
    mixins.SoftDeleteMixin,
    mixins.AuditMixin,
    mixins.SlugMixin,
    mixins.ActiveMixin,
    mixins.ImageMixin,
    mixins.ParentChildMixin,
    models.Model,
):
    """Course Model."""

    requirements = models.ManyToManyField(
        Requirement, related_name="courses", blank=True
    )
    prerequisites = models.ManyToManyField(
        "self", symmetrical=False, related_name="leads_to", blank=True
    )
    tags = TaggableManager()

    duration_in_days = models.PositiveIntegerField(default=0)
    popularity = models.PositiveIntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:show", kwargs={"course_slug": self.slug})

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["slug", "popularity"])]
