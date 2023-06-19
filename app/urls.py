from django.contrib import admin
from django.urls import path
from app import views


urlpatterns=[

    path('admin/', admin.site.urls),
    path('', views.inicio, name="Inicio"),
    path('aio/', views.aio, name="Aio"),
    path('desktop/', views.desktop, name="Desktop"),
    path('celulares/', views.celulares, name="Celulares"),
    path('notebook/', views.notebook, name="Notebook"),
    path('login/', views.login, name="Login"),
    path('form_api/', views.formularioapi, name="Formularioapi"),
    path('buscar_notebooks/', views.buscar_notebooks, name="Buscar_notebooks"),
    path('Mostrar_notebooks/', views.Mostrar_notebooks, name="Mostrar_notebooks"),

]

