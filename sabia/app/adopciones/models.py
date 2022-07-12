from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


from django.utils.text import slugify
class Categorias_Perros(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Categorias_Perros, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Pagina_adopciones2', args=[self.slug])


class Perros(models.Model):
    category = models.ForeignKey(Categorias_Perros, related_name='categoria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True, verbose_name='Nombres')
    raza = models.CharField(max_length=50, blank=True, verbose_name='Raza')
    edad =models.CharField(max_length=20,blank=True,verbose_name="edad")
    vacunas = models.CharField(max_length=10,blank=True, verbose_name="Vacunas" )
    enfermedades = models.CharField(max_length=100,blank=True, verbose_name="Enfermedades")
    estado = models.BooleanField(default=False, verbose_name='Estado')
    descripcion = models.TextField(blank=True, verbose_name='Descripcion')
    link = models.URLField(null=True, blank=True, verbose_name="Red Social")
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

