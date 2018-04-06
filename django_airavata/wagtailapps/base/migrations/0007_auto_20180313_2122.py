# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_wagtail_base', '0006_auto_20180313_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footertext',
            name='image_class_name',
        ),
        migrations.AddField(
            model_name='footertext',
            name='image_id_name',
            field=models.CharField(blank=True, help_text='Give a custom id name', max_length=255, null=True),
        ),
    ]