# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("dataedit", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="tablerevision",
            name="file",
            field=models.FileField(default=None, upload_to="dumps"),
            preserve_default=False,
        )
    ]
