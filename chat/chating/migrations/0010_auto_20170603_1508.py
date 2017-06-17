# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-03 15:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chating', '0009_auto_20170603_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]