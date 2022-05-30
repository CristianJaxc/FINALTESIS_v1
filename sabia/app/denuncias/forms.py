
from django import forms
from app.denuncias.models import Denuncias

class DenunciasForm(forms.ModelForm):
    nombres = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellidos = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    cedula= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nº de Identificacion')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Telefono')
    direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    #estado = forms.BooleanField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Estado')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    imagen=forms.ImageField(required=False,label='Foto Denuncia')
    class Meta:
        model = Denuncias
        fields = ['nombres', 'apellidos','cedula','telefono','direccion','descripcion','imagen']

class DenunciasForm2(forms.ModelForm):
    nombres = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellidos = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    cedula= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nº de Identificacion')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Telefono')
    direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    estado = forms.BooleanField(required=False,label='Estado de la denuncia')
    imagen=forms.ImageField(required=False,label='Foto Denuncia')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Denuncias
        fields = ['nombres', 'apellidos','cedula','telefono','direccion','estado','descripcion','imagen']