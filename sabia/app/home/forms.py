import email
from django import forms
from app.home.models import Contactos

class ContactosForm(forms.ModelForm):
    nombres = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres Completos')
    apellidos = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos completos')
    email= forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}),label='Email')
    telefono = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Teléfono')
    #direccion = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Direccion')
    #estado = forms.BooleanField(required=False,label='Estado de la denuncia')
    descripcion = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripción')
    class Meta:
        model = Contactos
        fields = ['nombres', 'apellidos','email','telefono','descripcion']