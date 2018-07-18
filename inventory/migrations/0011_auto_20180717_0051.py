# Generated by Django 2.0.4 on 2018-07-17 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20180716_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='bill_number',
            field=models.CharField(max_length=155, verbose_name='Número de Factura'),
        ),
        migrations.AlterField(
            model_name='item',
            name='barcode_number',
            field=models.CharField(blank=True, default='', max_length=155, unique=True, verbose_name='Código de barras'),
        ),
    ]