
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contactos(models.Model):
    nombres = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, blank=True, verbose_name='Apellidos')
    email =models.EmailField(blank=True,verbose_name="Email")
    telefono = models.CharField(max_length=10,blank=True, verbose_name="Telefono" )
    direccion= models.CharField(max_length=100,blank=True, verbose_name="Direccion")
    estado = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')


