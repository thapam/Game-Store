# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0008_auto_20160129_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default='', max_length=32),
        ),
    ]
