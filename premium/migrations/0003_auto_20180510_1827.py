# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 18:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0002_auto_20180510_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiredate',
            field=models.DateField(default=datetime.datetime(2018, 6, 9, 18, 27, 20, 615461)),
        ),
    ]
