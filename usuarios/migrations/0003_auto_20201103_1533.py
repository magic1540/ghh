# Generated by Django 3.1.1 on 2020-11-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20201101_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='/static/imagenes/img_estandar_usuario.jpg', null=True, upload_to='perfil', verbose_name='Imagen de perfil'),
        ),
    ]