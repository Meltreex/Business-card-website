from django.shortcuts import render

def about(requests):
    return render(requests, 'about/about.html')
