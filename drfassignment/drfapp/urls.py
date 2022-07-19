from django.contrib import admin
from django.urls import path
from drfapp.views import courseListView, courseDetailsListView
urlpatterns = [
    path('courses', courseListView),
    path('courses/<int:pk>', courseDetailsListView),
]
