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





class Noticia(models.Model):
    titulo = models.CharField(max_length=200, blank=True, verbose_name='Titulo de la publicacion')
    contenido_noticia = models.TextField(blank=True, verbose_name='Contenido de la publicacion')
    link = models.URLField(null=True, blank=True,verbose_name="Dirección Web")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    estado = models.BooleanField(default=False, verbose_name='Estado de la publicacion')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion de la publicacion')
    imagen_noticia=models.ImageField(upload_to='photos',verbose_name="imagenes",default='photos/perro1.jpg')

    class Meta:
            verbose_name = "noticia"
            verbose_name_plural = "noticias"
            ordering = ["-fecha_creacion"]

            def __str__(self):
                return self.title

