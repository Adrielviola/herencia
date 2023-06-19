from django.contrib import admin
from django.urls import path
from app import views


urlpatterns=[

    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('aio/', views.aio, name="aio"),
    path('desktop/', views.desktop, name="desktop"),
    path('celulares/', views.celulares, name="celulares"),
    path('notebook/', views.notebook, name="notebook"),
    path('login/', views.login, name="login"),
    path('form_api/', views.formularioapi, name="formularioapi"),


]

