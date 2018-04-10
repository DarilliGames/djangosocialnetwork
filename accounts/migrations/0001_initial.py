# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 11:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0005_publisher_img_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=200)),
                ('serious', models.BooleanField(default=True)),
                ('fun', models.BooleanField(default=True)),
                ('rank', models.IntegerField(blank=True, default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgame', to='games.Game')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=200)),
                ('bio', models.TextField()),
                ('is_youtube', models.BooleanField(default=False)),
                ('youtubelink', models.CharField(blank=True, max_length=200)),
                ('is_streamer', models.BooleanField(default=False)),
                ('streamkey', models.CharField(blank=True, max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('last_online', models.DateField(auto_now_add=True)),
                ('playing_game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='streamer', to='games.Game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
