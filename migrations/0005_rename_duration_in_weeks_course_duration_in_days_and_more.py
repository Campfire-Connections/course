# Generated by Django 5.0.6 on 2024-10-27 23:50

import django.db.models.deletion
import core.mixins.settings
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0004_alter_course_options_course_average_rating_and_more"),
        ("enrollment", "0006_facilityclass_max_enrollment_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="duration_in_weeks",
            new_name="duration_in_days",
        ),
        migrations.CreateModel(
            name="FacilityClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("max_enrollment", models.PositiveIntegerField(default=30)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created_%(class)s_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "facility_enrollment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="facility_classes",
                        to="enrollment.facilityenrollment",
                        verbose_name="Facility Enrollment",
                    ),
                ),
                (
                    "last_activity_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="last_activity_%(class)s_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="facility_classes",
                        to="enrollment.organizationcourse",
                        verbose_name="Organization Course",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="updated_%(class)s_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Facility Class",
                "verbose_name_plural": "Facility Classes",
                "ordering": ["name"],
                "indexes": [
                    models.Index(
                        fields=["slug", "name"], name="course_faci_slug_13e438_idx"
                    )
                ],
            },
            bases=(core.mixins.settings.SettingsMixin, models.Model),
        ),
    ]
