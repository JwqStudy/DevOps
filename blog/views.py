from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blogIndex(request):
    return render(request, 'blog.html')