# course/admin.py

from django.contrib import admin

from .models.course import Course
from .models.facility_class import FacilityClass
from .models.requirement import Requirement

admin.site.register(Course)
admin.site.register(FacilityClass)
admin.site.register(Requirement)
