# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170605_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendgroup',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]