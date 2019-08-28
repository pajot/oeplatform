# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modelview", "0007_auto_20160229_1630")]

    operations = [
        migrations.RemoveField(
            model_name="energymodel", name="typical_computation_time_less_than_a_day"
        ),
        migrations.RemoveField(
            model_name="energymodel", name="typical_computation_time_less_than_a_minute"
        ),
        migrations.RemoveField(
            model_name="energymodel", name="typical_computation_time_less_than_a_second"
        ),
        migrations.RemoveField(
            model_name="energymodel", name="typical_computation_time_less_than_an_hour"
        ),
        migrations.RemoveField(
            model_name="energymodel", name="typical_computation_time_more_than_a_day"
        ),
        migrations.AddField(
            model_name="energymodel",
            name="observation_period_less_1_year",
            field=models.BooleanField(default=False, verbose_name="<1 year"),
        ),
        migrations.AddField(
            model_name="energymodel",
            name="observation_period_more_1_year",
            field=models.BooleanField(default=False, verbose_name=">1 year"),
        ),
        migrations.AddField(
            model_name="energymodel",
            name="observation_period_other",
            field=models.BooleanField(default=False, verbose_name="other"),
        ),
        migrations.AddField(
            model_name="energymodel",
            name="observation_period_other_text",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="energymodel",
            name="typical_computation_time",
            field=models.CharField(
                choices=[
                    ("less than a second", "less than a second"),
                    ("less than a minute", "less than a minute"),
                    ("less than an hour", "less than an hour"),
                    ("less than a day", "less than a day"),
                    ("more than a day", "more than a day"),
                ],
                default="less than a minute",
                max_length=30,
            ),
            preserve_default=False,
        ),
    ]
