# Generated by Django 2.1.2 on 2019-04-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190427_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estudio',
            field=models.CharField(max_length=50),
        ),
    ]
