from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Saltstack')

def installApp(request):
    return render(request, 'installapp.html')