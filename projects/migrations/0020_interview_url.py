# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20180203_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
