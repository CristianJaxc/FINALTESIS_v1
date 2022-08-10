

from django.db import models
from django.forms import model_to_dict

from django.urls import reverse


from django.utils.text import slugify

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self,exclude='image')
        #item['category'] = self.category.toJSON()
        #item['name'] = self.name.toJSON()
        #item['slug'] = self.slug.toJSON()
        #item['description'] = self.description.toJSON()
        #item['price'] = self.price.toJSON()
        # item['stock'] = self.stock.toJSON()
        # item['available'] = self.available.toJSON()
        #item['created'] = self.created.toJSON()
        #item['updated'] = self.updated.toJSON()
        return item

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])




class ImagenProducto(models.Model):

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    producto = models.ForeignKey(Product, related_name='imagenes', on_delete=models.CASCADE, )
