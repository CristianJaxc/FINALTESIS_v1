
from django import forms
from app.adopciones.models import Perros, Solicitudes

class PerroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre')
    raza = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='raza')
    edad= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Edad')
    vacunas = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Vacunas')
    enfermedades = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Enfermedades')
    estado = forms.BooleanField(required=False,label='Estado del perro')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    imagen_mascota=forms.ImageField(required=False,label='Foto Perro')
    class Meta:
        model = Perros
        fields = ['nombre','raza','edad','vacunas','enfermedades','estado','descripcion','imagen_mascota']


class SolicitudesForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellido = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    cedula= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nº de Identificacion')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Telefono')
    direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    #estado = forms.BooleanField(required=False,label='Estado de la denuncia')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Solicitudes
        fields = ['nombre', 'apellido','cedula','telefono','direccion','descripcion']

class SolicitudesForm2(forms.ModelForm):
    nombre = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellido = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    cedula= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nº de Identificacion')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Telefono')
    direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    estado = forms.BooleanField(required=False,label='Estado de la solicitud')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Solicitudes
        fields = ['nombre', 'apellido','cedula','telefono','direccion','estado','descripcion']
