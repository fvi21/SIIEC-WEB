# Generated by Django 2.1.2 on 2019-05-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitucionMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreInstitucion', models.CharField(max_length=60, verbose_name='Nombre de institucion')),
                ('calle', models.CharField(max_length=60, verbose_name='Calle')),
                ('barrio', models.CharField(max_length=60, verbose_name='Barrio')),
                ('numeracion', models.IntegerField(verbose_name='Numeracion')),
                ('pais', models.CharField(max_length=60, verbose_name='Pais')),
                ('ciudad', models.CharField(max_length=60, verbose_name='Ciudad')),
                ('provinciaEstado', models.CharField(max_length=60, verbose_name='Provincia')),
                ('codPostal', models.IntegerField(verbose_name='Codigo postal')),
                ('servicioRx', models.BooleanField(default=False, verbose_name='Servicio RX')),
                ('servicioFluoro', models.BooleanField(default=False, verbose_name='Servicio Fluoro')),
                ('servicioArococ', models.BooleanField(default=False, verbose_name='Servicio ArocoC')),
            ],
        ),
    ]
