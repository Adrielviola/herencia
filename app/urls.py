from django.contrib import admin
from django.urls import path
from app import views


urlpatterns=[

    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('notebook/', views.notebook, name="notebook"),
    path('aio/', views.aio, name="aio"),
    path('Desktop/', views.desktop, name="desktop"),
    path('celulares', views.celulares, name="celulares"),
    path('login', views.login, name="login"),

    ]

