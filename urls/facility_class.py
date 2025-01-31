# course/urls/facility_class.py

from django.urls import path
from ..views.facility_class import (
    ListView, CreateView, UpdateView, DeleteView, ShowView
)

app_name = 'facility_class'

urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('new/', CreateView.as_view(), name='new'),
    path('<int:pk>/edit/', UpdateView.as_view(), name='edit'),
    path('<slug:facility_class_slug>/edit/', UpdateView.as_view(), name='edit'),
    path('<slug:facility_class_slug>/', ShowView.as_view(), name="show"),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<slug:facility_class_slug>/delete/', DeleteView.as_view(), name='delete'),
]
