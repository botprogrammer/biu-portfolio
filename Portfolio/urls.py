from django.contrib import admin
from django.urls import path, include
import portapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portapp.urls')),
]
