from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse ("This is a specific blog post.")

# def article(request, article_id):
#     return render(request, 'blog/article.html', {'article_id': article_id})

def getResponse(request):
    userMessage = request.GET.get('userMessage') # get the user's message from the query string from index.html
    return HttpResponse(userMessage)