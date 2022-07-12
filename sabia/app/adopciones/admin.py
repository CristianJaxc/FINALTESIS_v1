from django.contrib import admin
from .models import Perros, Solicitudes, Categorias_Perros

# Register your models here.
admin.site.register(Perros)
admin.site.register(Categorias_Perros)