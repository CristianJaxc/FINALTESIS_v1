# Generated by Django 3.0.8 on 2022-06-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20220227_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen_perfil',
            field=models.ImageField(default='photos/donacion1.jpg', upload_to='photos', verbose_name='imagenes'),
        ),
    ]