# Generated by Django 2.1.2 on 2019-05-06 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190502_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='pertimetroAbdominal',
            new_name='perimetroAbdominal',
        ),
    ]
