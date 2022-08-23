from django import forms

from .models import Order

from crispy_forms.helper import FormHelper
class OrderCreateForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ['first_name','last_name','email', 'address', 'postal_code',
                  'city','image','paid']

    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu Nombre  '}),label='Nombre')
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu Apellido  '}),label='Apellido')
    email= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu correo '}),label='Email')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu direccion  '}),label='Ubicacion')
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el codigo Postal'}),label='Codigo Postal ')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la ciudad '}),label='Ciudad')


class OrderCreatePaypalForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ['first_name','last_name','email', 'address', 'postal_code',
                  'city']

    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu Nombre  '}),label='Nombre')
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu Apellido  '}),label='Apellido')
    email= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu correo '}),label='Email')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu direccion  '}),label='Ubicacion')
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el codigo Postal'}),label='Codigo Postal ')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la ciudad '}),label='Ciudad')
