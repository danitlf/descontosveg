# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'img', verbose_name='Imagem:'),
        ),
        migrations.AddField(
            model_name='sale',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'img', verbose_name='Imagem:'),
        ),
    ]
