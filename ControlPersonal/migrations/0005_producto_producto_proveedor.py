# Generated by Django 3.1.4 on 2022-07-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0004_auto_20220718_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='producto_proveedor',
            field=models.ManyToManyField(to='ControlPersonal.Proveedor'),
        ),
    ]
