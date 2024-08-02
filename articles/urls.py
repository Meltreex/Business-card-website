from django.urls import path, include
from . import views

urlpatterns = [
    path('articles', views.articles, name='articles'),
    path('articles/articles-detail/<int:pk>/', views.ArticlesDetailView.as_view(), name='articles-detail'),
]
