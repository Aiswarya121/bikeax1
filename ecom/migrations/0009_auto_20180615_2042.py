# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-15 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_auto_20180615_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orders',
            new_name='user',
        ),
    ]