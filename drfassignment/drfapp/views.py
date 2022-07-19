from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drfapp.models import Course
from drfapp.serializers import CourseSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def courseListView(request):
    if request.method == 'GET':
        course = Course.objects.all()
        course_serializer = CourseSerializer(course, many = True)
        return Response(course_serializer.data)
    elif request.method == 'POST':
        course_serializer = CourseSerializer(data = request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(course_serializer.errors)
@api_view(['GET', 'PUT', 'DELETE'])
def courseDetailsListView(request, pk):
    try:
        course = Course.objects.get(pk = pk)
    except Course.DoesNotExist:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == 'DELETE':
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        course_serializer = CourseSerializer(course)
        return Response(course_serializer.data)
    elif request.method == 'PUT':
        course_serializer = CourseSerializer(course, data = request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        else:
            return Response(course_serializer.errors)
