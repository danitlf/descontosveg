# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moip', '0008_auto_20170310_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_sales',
            name='state',
            field=models.CharField(choices=[('0', 'Utilizado'), ('1', 'Disponivel')], max_length=1, verbose_name='status'),
        ),
    ]