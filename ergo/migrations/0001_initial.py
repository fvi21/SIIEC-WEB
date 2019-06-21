# Generated by Django 2.1.2 on 2019-05-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_estudio_instituciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ergometria',
            fields=[
                ('id_ergo', models.AutoField(primary_key=True, serialize=False)),
                ('ciclo_ergo', models.BooleanField(default=False)),
                ('banda_ergo', models.BooleanField(default=False)),
                ('st', models.CharField(max_length=50)),
                ('ta_plana', models.BooleanField(default=False)),
                ('motivo_suspencion', models.CharField(max_length=50)),
                ('arritmia_sv', models.CharField(max_length=50)),
                ('arritmia_v', models.CharField(max_length=50)),
                ('sintomas', models.CharField(max_length=50)),
                ('paciente_ergo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pacientes')),
            ],
        ),
    ]
