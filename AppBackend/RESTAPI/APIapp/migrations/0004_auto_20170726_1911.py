# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-26 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0003_auto_20170726_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='mapImage',
            new_name='mapFilePath',
        ),
    ]
