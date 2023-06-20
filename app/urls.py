from django.contrib import admin
from django.urls import path
from app import views
from app import class_views

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
    path('borrar/<id>/', views.borrar, name="Borrar"),

]

urlpatterns += [

    path('notebooklist/', class_views.NotebooksListView.as_view() , name="NotebooksList"),
    path('notebookdetail/<int:pk>/', class_views.NotebooksDetailView.as_view() , name="NotebooksDetail"),
    path('notebookcreate/', class_views.NotebooksCreateView.as_view() , name="NotebooksCreate"),
    path('notebookupdate/<int:pk>/', class_views.NotebooksUpdateView.as_view() , name="Notebooksupdate"),
    path('notebookdelete/<int:pk>/', class_views.NotebooksDeleteView.as_view() , name="NotebooksDelete"),    
]
