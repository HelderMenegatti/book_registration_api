# Generated by Django 3.2.1 on 2021-05-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Descricao_rapida',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
