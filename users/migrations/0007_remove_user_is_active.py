# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 05:35
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170215_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
