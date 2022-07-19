from django import views
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('view_books/', views.view_books, name='view_books'),
]
