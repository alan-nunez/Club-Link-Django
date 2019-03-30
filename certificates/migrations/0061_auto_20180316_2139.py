# Generated by Django 2.0.2 on 2018-03-16 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0060_auto_20180309_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='staging_code',
            field=models.CharField(blank=True, max_length=13, verbose_name='Staging Code'),
        ),
        migrations.AddField(
            model_name='departmentcertificatetype',
            name='staging_guid',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Staging GUID'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='code',
            field=models.CharField(blank=True, max_length=13, unique=True, verbose_name='Production Code'),
        ),
        migrations.AlterField(
            model_name='departmentcertificatetype',
            name='guid',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Production GUID'),
        ),
    ]
