# Generated by Django 3.1.4 on 2022-07-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
