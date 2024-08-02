from django.urls import path, include
from . import views

urlpatterns = [
    path('projects', views.projects, name='projects'),
    path('projects/projects-detail/<int:pk>/', views.ProjectsDetailView.as_view(), name='projects-detail'),
]
