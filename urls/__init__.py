# course/urls/__init__.py

from django.urls import path, include

urlpatterns = [
    path('courses/', include('course.urls.course')),
    path('requirements/', include('course.urls.requirement')),
    path('facility-classes/', include('course.urls.facility_class')),
]