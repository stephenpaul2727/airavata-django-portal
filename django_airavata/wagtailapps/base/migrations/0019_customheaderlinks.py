# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_wagtail_base', '0018_contactpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomHeaderLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_link_text', models.CharField(help_text='Give a Link text', max_length=25)),
                ('header_link', models.CharField(blank=True, help_text='Provide a redirect Link', max_length=255, null=True)),
                ('header_sub_link_text1', models.CharField(blank=True, help_text='Give a Sub Link 1 text', max_length=25, null=True)),
                ('header_sub_link_text2', models.CharField(blank=True, help_text='Give a Sub Link 2 text', max_length=25, null=True)),
                ('header_sub_link_text3', models.CharField(blank=True, help_text='Give a Sub Link 3 text', max_length=25, null=True)),
                ('header_sub_link_text4', models.CharField(blank=True, help_text='Give a Sub Link 4 text', max_length=25, null=True)),
                ('header_sub_link1', models.CharField(blank=True, help_text='Provide a redirect Link for sublink 1', max_length=255, null=True)),
                ('header_sub_link2', models.CharField(blank=True, help_text='Provide a redirect Link for sublink 2', max_length=255, null=True)),
                ('header_sub_link3', models.CharField(blank=True, help_text='Provide a redirect Link for sublink 3', max_length=255, null=True)),
                ('header_sub_link4', models.CharField(blank=True, help_text='Provide a redirect Link for sublink 4', max_length=255, null=True)),
                ('body', models.CharField(blank=True, help_text='Give a title text', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Header Custom Links',
            },
        ),
    ]