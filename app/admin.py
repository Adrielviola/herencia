from django.contrib import admin
from .models import Notebook, Aio, Desktop, Celulares, Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','email','dni']
    search_fields = ('nombre', 'apellido','email','dni',)
    ordering =  ('nombre', 'apellido','email','dni',)
    List_editable = ['nombre', 'apellido','email','dni']   

@admin.register(Aio)
class AioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','serie','dni']
    search_fields = ('nombre', 'apellido','marca','modelo','serie','dni',)
    ordering =  ('nombre', 'apellido','marca','modelo','serie','dni',)
    List_editable = ['nombre', 'apellido','marca','modelo','serie','dni']

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','serie','dni']
    search_fields = ('nombre', 'apellido','marca','modelo','serie','dni',)
    ordering = ('nombre', 'apellido','marca','modelo','serie','dni',)
    List_editable = ['nombre', 'apellido','marca','modelo','serie','dni']

@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','serie','dni']
    search_fields = ('nombre', 'apellido','marca','modelo','serie','dni',)
    ordering = ('nombre', 'apellido','marca','modelo','serie','dni',)
    List_editable = ['nombre', 'apellido','marca','modelo','serie','dni']

@admin.register(Celulares)
class CelularesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','marca','modelo','imei','dni']
    search_fields = ('nombre', 'apellido','marca','modelo','imei','dni',)
    ordering = ('nombre', 'apellido','marca','modelo','imei','dni',)
    List_editable = ['nombre', 'apellido','marca','modelo','imei','dni']

# Register your models here.
