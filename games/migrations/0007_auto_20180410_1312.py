# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20180410_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='reviews_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='reviews_score',
            field=models.IntegerField(default=0),
        ),
    ]
