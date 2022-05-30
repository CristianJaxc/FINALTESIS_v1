from django import forms
from app.servicios.models import Product ,ImagenProducto,  Category

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ImagenesForm(forms.ModelForm):
    class Meta:
        model = ImagenProducto

        fields = '__all__'

