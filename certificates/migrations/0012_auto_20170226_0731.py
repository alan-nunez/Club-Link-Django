# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-26 07:31
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0011_auto_20170226_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatetype',
            name='cart_included',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='certificatetype',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='certificatetype',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]