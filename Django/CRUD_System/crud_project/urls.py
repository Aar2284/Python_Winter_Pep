from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD_system.urls')),
    path('api/', include('Rest_Framework.urls')),
]
