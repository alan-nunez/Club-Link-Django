# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-21 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20170221_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='is_system_page',
        ),
        migrations.AddField(
            model_name='page',
            name='is_locked',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
