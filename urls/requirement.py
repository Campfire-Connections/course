# course/urls/requirement.py

from django.urls import path
from ..views.requirement import (
    ListView, CreateView,
    UpdateView, DeleteView
)

app_name = 'requirements'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('new/', CreateView.as_view(), name='create'),
    path('<int:pk>/edit/', UpdateView.as_view(), name='update'),
    path('<slug:slug>/edit/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<slug:slug>/delete/', DeleteView.as_view(), name='delete'),
]
