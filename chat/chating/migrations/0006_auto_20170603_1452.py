# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-03 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chating', '0005_group_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='chat',
            field=models.ManyToManyField(blank=True, null=True, to='chating.Chat'),
        ),
    ]