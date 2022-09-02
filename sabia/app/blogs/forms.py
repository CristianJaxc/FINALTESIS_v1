from django import forms
from app.blogs.models import Blogs,Noticia,NotiInfo

class BlogsForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Título')
    #fecha_creacion = forms.DateField(widget = forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),label='Fecha del blog', help_text="El formato es: 24/12/2020")
    #estado = forms.BooleanField(required=False,label='Estado de la solicitud')
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripcción')
    class Meta:
        model = Blogs
        fields = ['titulo','descripcion']

class BlogsForm2(forms.ModelForm):
    titulo = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),label='Titulo')
    #fecha_creacion = forms.DateField(widget = forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),label='Fecha del blog', help_text="El formato es: 24/12/2020")
    estado = forms.BooleanField(required=False,label='Estado de la solicitud')
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label='Descripccion')
    class Meta:
        model = Blogs
        fields = ['titulo','estado','descripcion']


class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = '__all__'


class NoticiaBlogForm(forms.ModelForm):
    class Meta:
        model = NotiInfo
        fields = '__all__'
