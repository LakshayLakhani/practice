# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_extendgroup_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendgroup',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
