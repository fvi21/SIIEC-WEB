# Generated by Django 2.1.2 on 2019-05-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ergo', '0002_auto_20190524_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergometria',
            name='carga',
            field=models.IntegerField(null=True, verbose_name='Carga'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='fc_basal',
            field=models.IntegerField(null=True, verbose_name='Fc basal'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='fc_esfuerzo',
            field=models.IntegerField(null=True, verbose_name='Fc esfuerzo'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='fcm_edad',
            field=models.IntegerField(null=True, verbose_name='Fcm edad'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='itt',
            field=models.IntegerField(null=True, verbose_name='Itt'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='mets',
            field=models.IntegerField(null=True, verbose_name='Mets'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='percent_fcmp',
            field=models.IntegerField(null=True, verbose_name='Percent fcmp'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='st_mm',
            field=models.IntegerField(null=True, verbose_name='St mm'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='tad_basal',
            field=models.IntegerField(null=True, verbose_name='Tad basal'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='tad_esfuerzo',
            field=models.IntegerField(null=True, verbose_name='Tad esfuerzo'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='tas_basal',
            field=models.IntegerField(null=True, verbose_name='Tas basal'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='tas_esfuerzo',
            field=models.IntegerField(null=True, verbose_name='Tas esfuerzo'),
        ),
    ]
