# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-30 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_wagtail_base', '0066_auto_20180330_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='announcement_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='announcement_text',
        ),
    ]