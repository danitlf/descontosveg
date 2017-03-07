# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='partner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.Partner'),
            preserve_default=False,
        ),
    ]
