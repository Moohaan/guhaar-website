# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-03 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20180202_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_started']},
        ),
    ]