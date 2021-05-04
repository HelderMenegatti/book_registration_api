# Generated by Django 3.2.1 on 2021-05-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=250)),
                ('ISBN', models.CharField(max_length=25)),
                ('Autor', models.CharField(max_length=250)),
                ('Editora', models.CharField(max_length=250)),
                ('Edicao', models.CharField(max_length=250)),
                ('Numero_de_paginas', models.IntegerField()),
            ],
        ),
    ]
