# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart2',
            name='product',
            field=models.CharField(max_length=25),
        ),
    ]
