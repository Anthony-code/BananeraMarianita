# Generated by Django 3.1.4 on 2022-07-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0015_auto_20220720_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
