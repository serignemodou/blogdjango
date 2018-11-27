from django.shortcuts import render, get_object_or_404
from django.http import Http404
#from .mocks import Article
from .models import Article

def index(request):
    article=Article.objects.all()
    return render(request, 'blog/index.html', {'articles':article})

def show(request, id):
    article=get_object_or_404(Article, pk=id)
    return render(request, 'blog/show.html', {'articles':article})
