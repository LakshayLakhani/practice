# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-03 14:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chating', '0004_auto_20170603_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
