from ast import Return
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet
from cbvapp.models import Course, CourseSerializer

# Create your views here.
# """ModelViewSets"""

class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    
#"""ViewSets"""
'''
class CourseViewSet(ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        course_serializer = CourseSerializer(courses, many = True)
        return Response(course_serializer.data)

    def retrieve(self, request, pk):
        try:
            courses = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status= status.HTTP_204_NO_CONTENT)
        course_serializer = CourseSerializer(courses)
        return Response(course_serializer.data)
    
    def create(self, request):
        courses = Course.objects.all()
        course_serializer = CourseSerializer(data = request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors)

    def destroy(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status= status.HTTP_204_NO_CONTENT)
        course.delete()
        return Response(status= status.HTTP_202_ACCEPTED)

    
    def update(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status= status.HTTP_204_NO_CONTENT)
        course_serializer = CourseSerializer(course, data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors)

'''


# """Using Generics"""
'''
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class DetailsCourseListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''
'''
class DetailsCourseListView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''
#"""Using Generics"""

'''
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class DetailsCourseListView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''

# """Using Mixin Classes and Generics"""
'''
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class DetailsCourseListView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

#"""Using ClassBasedViews"""

'''
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        course_serializer = CourseSerializer(courses, many = True)
        return Response(course_serializer.data)
    
    def post(self, request):
        courses = Course.objects.all()
        course_serializer = CourseSerializer(data = request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(course_serializer.errors)

class DetailsCourseListView(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        courses = self.get_course(pk)
        course_serializer = CourseSerializer(courses)
        return Response(course_serializer.data)


    def put(self, request, pk):
        courses = self.get_course(pk)
        course_serializer = CourseSerializer(courses, data = request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        else:
            return Response(course_serializer.errors)
    def delete(self, request, pk):
        courses = self.get_course(pk)
        courses.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
    '''