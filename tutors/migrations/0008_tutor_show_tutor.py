# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0007_auto_20171119_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='show_tutor',
            field=models.BooleanField(default=True),
        ),
    ]
