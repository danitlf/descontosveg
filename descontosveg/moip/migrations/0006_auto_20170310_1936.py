# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moip', '0005_auto_20170310_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='state',
            field=models.CharField(choices=[('1', 'Autorizado'), ('2', 'Iniciado'), ('3', 'Boleto Impresso'), ('4', 'Concluido'), ('5', 'Cancelado'), ('6', 'Em analise'), ('7', 'Estornado'), ('9', 'Reembolsado')], max_length=200, verbose_name='status'),
        ),
    ]
