# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-26 12:35
from __future__ import unicode_literals

from django.db import migrations, models


def populate_name(apps, schema_editor):
    ClubPage = apps.get_model('cms', 'ClubPage')
    CorpPage = apps.get_model('cms', 'CorpPage')

    for p in ClubPage.objects.all():
        p.name = 'Home' if p.slug == '' else p.slug
        p.save()

    for p in CorpPage.objects.filter(slug='home', parent=None):
        p.name = 'Home' if p.slug == '' else p.slug
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_auto_20170625_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubpage',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corppage',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.
        RunPython(populate_name),
    ]