# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='ward',
            field=models.CharField(db_index=True, max_length=10, null=True),
        ),
    ]