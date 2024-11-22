# course/forms/requirement.py

from django import forms
from ..models.requirement import Requirement

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
