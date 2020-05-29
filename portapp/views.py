from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "portapp/index.html"

class AboutView(TemplateView):
    template_name = "portapp/about.html"

class ProjectsView(TemplateView):
    template_name = "portapp/projects.html"

class ProjectsDetailView(TemplateView):
    template_name = "portapp/projects.html"

class ContactView(TemplateView):
    template_name = "portapp/worktogether.html"