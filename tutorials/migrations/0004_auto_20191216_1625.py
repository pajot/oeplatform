# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-16 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0003_tutorial_media"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutorial",
            name="media",
            field=models.URLField(blank=True, null=True),
        ),
    ]
