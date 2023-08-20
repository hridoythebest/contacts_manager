from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_contacts, name='list_contacts'),
    path('create/', views.create_contact, name='create_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]