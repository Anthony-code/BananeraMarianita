# Generated by Django 3.1.4 on 2022-08-05 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0024_auto_20220804_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='number_hour',
        ),
    ]
