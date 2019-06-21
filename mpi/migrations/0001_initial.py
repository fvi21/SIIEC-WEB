# Generated by Django 2.1.2 on 2019-05-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mpi',
            fields=[
                ('id_mpi', models.AutoField(primary_key=True, serialize=False)),
                ('s1_rest', models.FloatField(null=True)),
                ('s2_rest', models.FloatField(null=True)),
                ('s3_rest', models.FloatField(null=True)),
                ('s4_rest', models.FloatField(null=True)),
                ('s5_rest', models.FloatField(null=True)),
                ('s6_rest', models.FloatField(null=True)),
                ('s7_rest', models.FloatField(null=True)),
                ('s8_rest', models.FloatField(null=True)),
                ('s9_rest', models.FloatField(null=True)),
                ('s10_rest', models.FloatField(null=True)),
                ('s11_rest', models.FloatField(null=True)),
                ('s12_rest', models.FloatField(null=True)),
                ('s13_rest', models.FloatField(null=True)),
                ('s14_rest', models.FloatField(null=True)),
                ('s15_rest', models.FloatField(null=True)),
                ('s16_rest', models.FloatField(null=True)),
                ('s17_rest', models.FloatField(null=True)),
                ('s1_stress', models.FloatField(null=True)),
                ('s2_stress', models.FloatField(null=True)),
                ('s3_stress', models.FloatField(null=True)),
                ('s4_stress', models.FloatField(null=True)),
                ('s5_stress', models.FloatField(null=True)),
                ('s6_stress', models.FloatField(null=True)),
                ('s7_stress', models.FloatField(null=True)),
                ('s8_stress', models.FloatField(null=True)),
                ('s9_stress', models.FloatField(null=True)),
                ('s10_stress', models.FloatField(null=True)),
                ('s11_stress', models.FloatField(null=True)),
                ('s12_stress', models.FloatField(null=True)),
                ('s13_stress', models.FloatField(null=True)),
                ('s14_stress', models.FloatField(null=True)),
                ('s15_stress', models.FloatField(null=True)),
                ('s16_stress', models.FloatField(null=True)),
                ('s17_stress', models.FloatField(null=True)),
                ('s1_dif', models.FloatField(null=True)),
                ('s2_dif', models.FloatField(null=True)),
                ('s3_dif', models.FloatField(null=True)),
                ('s4_dif', models.FloatField(null=True)),
                ('s5_dif', models.FloatField(null=True)),
                ('s6_dif', models.FloatField(null=True)),
                ('s7_dif', models.FloatField(null=True)),
                ('s8_dif', models.FloatField(null=True)),
                ('s9_dif', models.FloatField(null=True)),
                ('s10_dif', models.FloatField(null=True)),
                ('s11_dif', models.FloatField(null=True)),
                ('s12_dif', models.FloatField(null=True)),
                ('s13_dif', models.FloatField(null=True)),
                ('s14_dif', models.FloatField(null=True)),
                ('s15_dif', models.FloatField(null=True)),
                ('s16_dif', models.FloatField(null=True)),
                ('s17_dif', models.FloatField(null=True)),
                ('ssr', models.FloatField(null=True)),
                ('sss', models.FloatField(null=True)),
                ('ssd', models.FloatField(null=True)),
            ],
        ),
    ]
