# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0003_auto_20180510_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='expiredate',
        ),
    ]
