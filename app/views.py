from django.shortcuts import render
from .models import Usuario


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

def formulario(request):
    if request.method == 'POST':
    
        print(f"\n\n\n{request.POST}\n")
# usuario(nuevo) =  Usuario (en mismo que en models.py)(request.POST['Usuario (en mismo que en models.py)'],(request.POST['dni(en mismo que en models.py']))
        usuario =  Usuario(nombre=request.POST['Usuario'], dni=request.POST['dni'])
        usuario.save()
        return render(request, "app/index.html")

    return render(request,"app/formulario.html")

