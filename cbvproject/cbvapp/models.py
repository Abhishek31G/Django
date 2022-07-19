from django.db import models
from dataclasses import fields
from rest_framework import serializers

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration = models.FloatField()
    authorname = models.CharField(max_length=30)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'