from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def index(request):
    return render(request, 'base.html')

def opsIndex(request):
    return render(request, 'index.html')

def publicIndex(request):
    return render(request, 'public.html')