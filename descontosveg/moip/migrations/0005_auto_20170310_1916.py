# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moip', '0004_auto_20170309_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF'),
        ),
    ]
