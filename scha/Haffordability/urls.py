from django.contrib import admin
from django.urls import path
from Haffordability import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.home, name='home'),
    path("index", views.index, name='index'),
    path("result", views.result),
]