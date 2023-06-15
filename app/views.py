from django.shortcuts import render
from .models import Notebook


def inicio(request):
    return render(request, "app/index.html")

def notebook(request):
    return render(request, "app/notebook.html")

def aio(request):
    return render(request, "app/aio.html")

def desktop(request):
    return render(request, "app/desktop.html")

def celulares(request):
    return render(request, "app/celulares.html")

def login(request):
    return render(request, "app/login.html")
