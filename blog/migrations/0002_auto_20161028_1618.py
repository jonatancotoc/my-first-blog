# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Actuacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('actor', models.ForeignKey(to='blog.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
                ('actores', models.ManyToManyField(to='blog.Actor', through='blog.Actuacion')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='actuacion',
            name='pelicula',
            field=models.ForeignKey(to='blog.Pelicula'),
        ),
    ]
