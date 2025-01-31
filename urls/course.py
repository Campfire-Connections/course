# course/urls/course.py

from django.urls import path
from ..views.course import (
    IndexView, CreateView,
    UpdateView, DeleteView
)

app_name = 'courses'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new/', CreateView.as_view(), name='new'),
    path('<int:pk>/edit/', UpdateView.as_view(), name='update'),
    path('<slug:slug>/edit/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<slug:slug>/delete/', DeleteView.as_view(), name='delete'),
]
