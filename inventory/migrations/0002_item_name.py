# Generated by Django 2.0.4 on 2018-07-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='Sin nombre', max_length=155),
            preserve_default=False,
        ),
    ]