from django.contrib import admin
from django.urls import path, include
import portapp

urlpatterns = [
    path('admin-only-biu/', admin.site.urls),
    path('', include('portapp.urls')),
]
