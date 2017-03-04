# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='descricao')),
                ('status', models.CharField(choices=[(b'd', b'Despublicado'), (b'p', b'Publicado')], max_length=1)),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='descricao')),
                ('status', models.CharField(choices=[(b'd', b'Despublicado'), (b'p', b'Publicado')], max_length=1)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='Livro')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
        ),
    ]
