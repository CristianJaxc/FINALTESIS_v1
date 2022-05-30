from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
    titulo = models.CharField( max_length=200 ,blank=True, verbose_name='Descripcion de la publicacion')
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    estado = models.BooleanField(default=False, verbose_name='Estado de la publicacion')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion de la publicacion')
    User = models.ForeignKey(User,on_delete=models.CASCADE)