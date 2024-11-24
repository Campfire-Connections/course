# course/models/requirement.py

from django.db import models
from django.urls import reverse


from core.mixins import models as mixins

class Requirement(
    mixins.NameDescriptionMixin,
    mixins.TimestampMixin,
    mixins.SoftDeleteMixin,
    mixins.AuditMixin,
    mixins.SlugMixin,
    mixins.ActiveMixin,
    mixins.ImageMixin,
    models.Model,
):
    """. Requirement Model."""

    #course = models.ForeignKey("course.Course", on_delete=models.CASCADE, related_name="requirements")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "requirements:show",
            kwargs={"slug": self.slug},
        )

