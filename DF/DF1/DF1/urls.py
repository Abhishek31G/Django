from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('df1app.urls')),
    path('', include('df1app2.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
