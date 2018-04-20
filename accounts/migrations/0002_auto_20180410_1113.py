# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='playing_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='streamers', to='games.Game'),
        ),
    ]