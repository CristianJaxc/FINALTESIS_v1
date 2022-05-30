from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perros(models.Model):
    nombre = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    raza = models.CharField(max_length=50, blank=True, verbose_name='Raza')
    edad =models.CharField(max_length=20,blank=True,verbose_name="edad")
    vacunas = models.CharField(max_length=10,blank=True, verbose_name="Vacunas" )
    enfermedades = models.CharField(max_length=100,blank=True, verbose_name="Enfermedades")
    estado = models.BooleanField(default=False, verbose_name='Estado')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')
    imagen_mascota=models.ImageField(upload_to='photos',verbose_name="imagenes",default='photos/perro1.jpg')


class Solicitudes(models.Model):
    nombre = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    apellido = models.CharField(max_length=50, blank=True, verbose_name='Apellidos')
    cedula = models.CharField(max_length=20,blank=True,verbose_name="Cedula o Pasaporte")
    telefono = models.CharField(max_length=10,blank=True, verbose_name="Telefono" )
    direccion = models.CharField(max_length=100,blank=True, verbose_name="Direccion")
    estado = models.BooleanField(default=False, verbose_name='Estado')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')
    perros = models.ForeignKey(Perros,verbose_name='Perros', on_delete=models.CASCADE)

