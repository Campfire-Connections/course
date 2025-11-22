# course/urls/course.py

from django.urls import path
from ..views.course import (
    CreateView,
    DeleteView,
    IndexView,
    ShowView,
    UpdateView,
)

app_name = 'courses'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new/', CreateView.as_view(), name='new'),
    path('<int:course_id>/', ShowView.as_view(), name='show_by_id'),
    path('<slug:course_slug>/', ShowView.as_view(), name='show'),
    path('<int:pk>/edit/', UpdateView.as_view(), name='update'),
    path('<slug:slug>/edit/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<slug:slug>/delete/', DeleteView.as_view(), name='delete'),
]
