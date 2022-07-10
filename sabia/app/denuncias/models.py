from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Denuncias(models.Model):
    nombres = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, blank=True, verbose_name='Apellidos')
    cedula =models.CharField(max_length=20,blank=True,verbose_name="Cedula o Pasaporte")
    telefono = models.CharField(max_length=10,blank=True, verbose_name="Telefono" )
    direccion= models.CharField(max_length=100,blank=True, verbose_name="Direccion")
    estado = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')
    imagen=models.ImageField(upload_to='photos',verbose_name="imagenes",default='photos/denuncia1.jpg')
 
