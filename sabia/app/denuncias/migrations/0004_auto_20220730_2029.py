# Generated by Django 3.0.8 on 2022-07-30 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0003_denuncias_fecha_creacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='denuncias',
            options={'ordering': ['id']},
        ),
    ]