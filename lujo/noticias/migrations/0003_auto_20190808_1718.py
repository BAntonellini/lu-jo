# Generated by Django 2.2.4 on 2019-08-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20190808_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]