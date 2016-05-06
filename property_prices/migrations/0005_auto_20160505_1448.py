# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_prices', '0004_auto_20160504_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'properties'},
        ),
        migrations.AlterField(
            model_name='property',
            name='paon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='saon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='property_prices.Property'),
        ),
    ]