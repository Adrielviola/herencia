from django.urls import path
from app import views


urlpatterns=[

    
    path('', views.inicio, name="Inicio"),
    path('notebook/', views.notebook, name="notebook"),
    path('aio/', views.aio, name="aio"),
    path('Desktop/', views.desktop, name="desktop"),
    path('celulares', views.celulares, name="celulares"),
    path('login', views.login, name="login"),
    path('formulario', views.inventarioFormulario, name="inventarioFormulario")
    ]

