# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-09 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20170606_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='user_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
