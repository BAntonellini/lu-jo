# Generated by Django 2.2.4 on 2019-08-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.SlugField(default='codigo', max_length=100, unique=True),
        ),
    ]