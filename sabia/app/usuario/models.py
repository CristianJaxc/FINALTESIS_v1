from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    imagen_perfil =models.ImageField(upload_to='photos',verbose_name="imagenes",default='photos/donacion1.jpg')
    cedula =models.CharField(max_length=20,blank=True,verbose_name="Cedula o Pasaporte")
    telefono = models.CharField(max_length=10,blank=True, verbose_name="Telefono" )
    direccion= models.CharField(max_length=100,blank=True, verbose_name="Direccion Domiciliaria")
    nacionalidad=models.CharField(max_length=100,verbose_name ='Nacionalidad',blank=True)
    User = models.OneToOneField(User,on_delete=models.CASCADE)