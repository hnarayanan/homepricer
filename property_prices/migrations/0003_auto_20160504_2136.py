# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_prices', '0002_auto_20160504_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transfer_date',
            field=models.DateField(null=True),
        ),
    ]