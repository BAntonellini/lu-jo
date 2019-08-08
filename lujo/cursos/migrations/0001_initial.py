# Generated by Django 2.2.4 on 2019-08-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20190808_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=100, verbose_name='Título del Curso')),
                ('resumen', models.TextField(max_length=500, verbose_name='Descripción del Curso')),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y hora')),
                ('imagen', models.ImageField(upload_to='cursos', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación')),
                ('tema', models.ManyToManyField(blank=True, null=True, to='core.Categoria', verbose_name='Temática')),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
