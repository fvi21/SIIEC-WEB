# Generated by Django 2.1.2 on 2019-05-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190427_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='apellidoNombre',
            field=models.CharField(max_length=50, verbose_name='Apellido y Nombre'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='calidadTecnica',
            field=models.IntegerField(verbose_name='Calidad tecnica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='coberturaMedica',
            field=models.CharField(max_length=50, verbose_name='Cobertura Medica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='decubito',
            field=models.CharField(max_length=50, verbose_name='Decubito'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.IntegerField(verbose_name='Dni'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estudio',
            field=models.CharField(max_length=50, verbose_name='Estudio'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaAcutal',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Actual'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='imc',
            field=models.IntegerField(verbose_name='Imc'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='indicacion',
            field=models.CharField(max_length=50, verbose_name='Indicacion'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='medico',
            field=models.CharField(max_length=50, verbose_name='Medico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observaciones',
            field=models.TextField(verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='pertimetroAbdominal',
            field=models.IntegerField(verbose_name='Perimetro Abdominal'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.FloatField(verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(max_length=20, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='supCorporal',
            field=models.FloatField(verbose_name='Superficie corporal'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='talla',
            field=models.FloatField(verbose_name='Talla'),
        ),
    ]
