# course/urls/requirement.py

from django.urls import path
from ..views.requirement import (
    ListView, ShowView, CreateView,
    UpdateView, DeleteView
)

app_name = 'requirements'

urlpatterns = [
    # Preferred names: index/new/show/edit/delete.
    # Legacy list/create/update names stay as compatibility aliases.
    path('', ListView.as_view(), name='index'),
    path('', ListView.as_view(), name='list'),
    path('new/', CreateView.as_view(), name='new'),
    path('new/', CreateView.as_view(), name='create'),
    path('<int:pk>/', ShowView.as_view(), name='show'),
    path('<slug:slug>/', ShowView.as_view(), name='show'),
    path('<int:pk>/edit/', UpdateView.as_view(), name='edit'),
    path('<int:pk>/edit/', UpdateView.as_view(), name='update'),
    path('<slug:slug>/edit/', UpdateView.as_view(), name='edit'),
    path('<slug:slug>/edit/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<slug:slug>/delete/', DeleteView.as_view(), name='delete'),
]
