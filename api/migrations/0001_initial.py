# Generated by Django 3.0.5 on 2020-05-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('salario', models.FloatField()),
                ('tipo_contrato', models.CharField(choices=[('CLT', 'Consolidação das Leis do Trabalho'), ('PJ', 'Pessoa Jurídica')], max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'vaga',
            },
        ),
    ]
