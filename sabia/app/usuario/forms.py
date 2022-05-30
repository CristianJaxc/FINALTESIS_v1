from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.usuario.models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'cedula',
            'direccion',
            'telefono',
            'nacionalidad',
        ]
        labels = {
            'cedula_perfil': 'Cédula',
            'direccion_perfil': 'Dirección',
            'telefono_perfil': 'Teléfono',
            'nacionalidad': 'Nacionalidad',
        }
        widgets = {
            'cedula_perfil': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_perfil': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_perfil': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'})
        }

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre de Usuario')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Correo Electrónico')
    first_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres')
    last_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos')
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name',]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form__field'}),
   
        }
