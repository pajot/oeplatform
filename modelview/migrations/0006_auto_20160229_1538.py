# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("modelview", "0005_auto_20160229_1532")]

    operations = [
        migrations.RemoveField(model_name="energyscenario", name="energy_saving_ne"),
        migrations.RemoveField(model_name="energyscenario", name="energy_saving_per"),
        migrations.RemoveField(model_name="energyscenario", name="energy_saving_until"),
        migrations.AddField(
            model_name="energyscenario",
            name="energy_saving_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="energy_saving_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="emission_reductions_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="potential_energy_savings_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_heat_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_mobility_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_power_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_total_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=15,
            ),
        ),
    ]
