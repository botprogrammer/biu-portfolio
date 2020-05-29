from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    AboutView,
    ProjectsView,
    ProjectsDetailView,
    ContactView
)

app_name = 'portapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/detail/<int:pk>/', ProjectsDetailView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
