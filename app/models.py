from django.db import models
#from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8)
    email = models.CharField(max_length=40)

class Notebook(models.Model):
# usuario_id = models.ForeignKey(usuario)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
class Desktop(models.Model):
    #usuario_id = models.ForeignKey(usuario)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni = models.CharField(max_length=8)

class Aio(models.Model):
    #usuario_id = models.ForeignKey(usuario)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni = models.CharField(max_length=8)

class Celulares(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=50)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    imei=models.DecimalField(max_digits=20, decimal_places=0)
    dni = models.CharField(max_length=8)
    
