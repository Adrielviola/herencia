from django.shortcuts import render, redirect
from .form import formulario_api, BuscarNotebooksForm
from .models import Notebook




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
    if request.method == 'POST':
        form = formulario_api(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formularioapi')
    else:
        form = formulario_api()

    return render(request, 'app/formulario_api.html', {'form': form})

def buscar_notebooks(request):
        form = BuscarNotebooksForm(request.POST)
        notebooks = None

        if form.is_valid():
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']

            notebooks = Notebook.objects.filter(marca=marca, modelo=modelo)

        context = {'form': form, 'notebooks': notebooks}
        return render(request, 'app/buscar_notebook.html', context)

def Mostrar_notebooks(request):

    notebooks = Notebook.objects.all() #trae todos los profesores

    contexto= {"notebooks":notebooks} 

    return render(request, "app/mostrar_notebooks.html",contexto)
