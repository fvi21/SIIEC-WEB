# Generated by Django 2.1.2 on 2019-05-22 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_institucionmedica'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudio',
            name='pacientes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pacientes'),
        ),
    ]
