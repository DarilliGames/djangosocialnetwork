# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_publisher_img_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
