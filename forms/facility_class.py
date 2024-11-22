# course/forms/facility_class.py

from django import forms
from enrollment.models.organization import OrganizationCourse
from ..models.facility_class import FacilityClass


class FacilityClassForm(forms.ModelForm):
    class Meta:
        model = FacilityClass
        fields = [
            "facility_enrollment",
            "organization_course",
            "start_time",
            "end_time",
            "max_enrollment",
        ]

    def __init__(self, *args, **kwargs):
        super(FacilityClassForm, self).__init__(*args, **kwargs)

        # Add CSS classes to the fields
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # Initially set organization_course queryset to empty
        self.fields["organization_course"].queryset = OrganizationCourse.objects.none()

        # Check if an instance with facility_enrollment exists
        if self.instance and self.instance.facility_enrollment:
            facility = self.instance.facility_enrollment.facility
            organization = facility.get_root_organization() if facility else None
            if organization:
                self.fields["organization_course"].queryset = (
                    OrganizationCourse.objects.filter(organization=organization)
                )
