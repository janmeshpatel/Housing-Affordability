from django.contrib import admin
from django.urls import path
from Haffordability import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services')
]