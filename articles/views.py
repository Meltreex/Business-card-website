from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

def articles(requests):
    art = Articles.objects.all()
    return render(requests, 'articles/articles.html', {'art': art})

class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'articles/details_view.html'
    context_object_name = 'articles'
