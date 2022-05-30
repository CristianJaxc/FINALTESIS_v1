import email
from django import forms
from app.donaciones.models import Solicitudes, Productos

class ProductosForm(forms.ModelForm):
    imagen=forms.ImageField(required=False,label='Foto Donacion')
    nombre = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre')
    cantidad = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='cantidad')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Productos
        fields = ['nombre','cantidad','descripcion','imagen']

class Solicitudes_donacion_Form(forms.ModelForm):
    nombre = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellido = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    cedula= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nº de Identificacion')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Telefono')
    email = forms.EmailField(required=True,label='Correo Electrónico')
    direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Solicitudes
        fields = ['nombre', 'apellido','cedula','telefono','email','direccion','descripcion']

class Solicitudes_donacion_Form2(forms.ModelForm):
    nombre = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellido = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    cedula= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nº de Identificacion')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Telefono')
    email = forms.EmailField(label='Correo Electrónico')
    direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    estado = forms.BooleanField(required=False,label='Estado de la solicitud')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Solicitudes
        fields = ['nombre', 'apellido','cedula','telefono','email','direccion','estado','descripcion']
