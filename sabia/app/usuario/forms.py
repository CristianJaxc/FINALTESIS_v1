from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.usuario.models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'imagen_perfil',
            'role',
            'cedula',
            'direccion',
            'telefono',
            'nacionalidad',
        ]
        labels = {
            'imagen_perfil':'imagen_perfil',
            'role':'Tipo de usuario',
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

class PerfilFormVoluntario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'imagen_perfil',
            'cedula',
            'direccion',
            'telefono',
            'nacionalidad',
        ]
        labels = {
            'imagen_perfil':'imagen_perfil',
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
    #username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombre de Usuario')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Correo Electrónico')
    first_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Nombres')
    last_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Apellidos')
    class Meta:
        model = User
        fields = [ 'email','first_name','last_name',]

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('email duplicado')

    # modificamos el método save() así podemos definir  user.is_active a False la primera vez que se registra

    #def clean_email(self):
    #    email= self.cleaned_data.get('email')
     #   if User.objects.filter(email=email).exists():
      #      raise forms.ValidationError(u'El email ya esta registrado prueba con otro')
       # return  email