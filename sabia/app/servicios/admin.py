from django.contrib import admin
from .models import Category,Product,ImagenProducto
# Register your models here.
class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductAdmin(admin.ModelAdmin):

    inlines = [
        ImagenProductoAdmin
    ]
admin.site.register(Product,ProductAdmin)
admin.site.register([Category])