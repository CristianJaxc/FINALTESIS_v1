import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime
class Productos(models.Model):
    imagen=models.ImageField(upload_to='photos',verbose_name="imagenes",default='photos/donacion1.jpg')
    nombre = models.CharField(max_length=50, blank=True, verbose_name='Nombre')
    cantidad = models.CharField(max_length=1000, blank=True, verbose_name='Cantidad')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')

class Solicitudes(models.Model):
    nombre = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    apellido = models.CharField(max_length=50, blank=True, verbose_name='Apellidos')
    cedula = models.CharField(max_length=20,blank=True,verbose_name="Cedula o Pasaporte")
    telefono = models.CharField(max_length=10,blank=True, verbose_name="Telefono" )
    email = models.EmailField(blank=True,verbose_name='Correo Electronico')
    date_joined = models.DateField(default=datetime.now)
    direccion = models.CharField(max_length=100,blank=True, verbose_name="Direccion")
    estado = models.BooleanField(default=False, verbose_name='Estado')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')
    productos = models.ForeignKey(Productos,verbose_name='Productos', on_delete=models.CASCADE)

