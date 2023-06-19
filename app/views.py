from django.shortcuts import render
from app.form import formulario_api
from .models import Usuario



def inicio(request):
    return render(request, "app/base.html")

def aio(request):
    return render(request, "app/aio.html")

def celulares(request):
    return render(request, "app/celulares.html")

def notebook(request):
    return render(request, "app/notebook.html")

def desktop(request):
    return render(request, "app/desktop.html")

def login(request):
    return render(request, "app/login.html")

def formularioapi(request):

    if request.method == "POST":
        miFormulario = formulario_api(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre=informacion["USUARIO"], dni=informacion["DNI"])
            usuario.save()
            return render(request, "app/base.html")
    else:
        miFormulario = formulario_api()

        print(miFormulario)

    return render(request, "app/formulario_api.html", {"miFormulario": miFormulario})