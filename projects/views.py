from django.shortcuts import render
from .models import Projects
from django.views.generic import DetailView

def projects(requests):
    prj = Projects.objects.all()
    return render(requests, 'projects/projects.html', {'prj': prj})

class ProjectsDetailView(DetailView):
    model = Projects
    template_name = 'projects/details_view.html'
    context_object_name = 'projects'