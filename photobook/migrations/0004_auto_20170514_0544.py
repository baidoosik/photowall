# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-14 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photobook', '0003_post_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
