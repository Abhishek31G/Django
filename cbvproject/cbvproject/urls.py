from django.contrib import admin
from django.urls import path, include
from django import views
from rest_framework.routers import DefaultRouter
# from cbvapp.views import CourseViewSet
from cbvapp.views import CourseModelViewSet

router = DefaultRouter()
router.register('courses', CourseModelViewSet, basename= 'course')
# router.register('courses', CourseViewSet, basename= 'course')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('cbvapp.urls')),
    path('api/', include(router.urls)),
]

