from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from django.contrib.auth.models import User

class Client(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=150,verbose_name='Nombres')
    last_name = models.CharField(max_length=150, verbose_name='Apellidos')
    email = models.EmailField()
    telefono = models.IntegerField()
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.username


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


