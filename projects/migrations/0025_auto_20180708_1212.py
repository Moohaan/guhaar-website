# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-08 12:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20180708_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
