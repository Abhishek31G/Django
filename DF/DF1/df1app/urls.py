from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('view_states/', views.view_states, name="view_states"),
]
