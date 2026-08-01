from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("todolist/", views.todolist, name="todolist"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
               ]
