# course/forms/course.py

from django import forms
from ..models.course import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "description", "image"]

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        #self.fields["active"].widget.attrs.update({"class": "form-control"})
