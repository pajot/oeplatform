# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("modelview", "0004_auto_20160228_2226")]

    operations = [
        migrations.RemoveField(
            model_name="energyscenario", name="emission_reductions_ne"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="emission_reductions_per"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="emission_reductions_until"
        ),
        migrations.RemoveField(model_name="energyscenario", name="name_of_study"),
        migrations.RemoveField(
            model_name="energyscenario", name="potential_energy_savings_ne"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="potential_energy_savings_per"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="potential_energy_savings_until"
        ),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_heat_ne"),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_heat_per"),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_heat_until"),
        migrations.RemoveField(
            model_name="energyscenario", name="share_RE_mobility_ne"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="share_RE_mobility_per"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="share_RE_mobility_until"
        ),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_power_ne"),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_power_per"),
        migrations.RemoveField(
            model_name="energyscenario", name="share_RE_power_until"
        ),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_total_ne"),
        migrations.RemoveField(model_name="energyscenario", name="share_RE_total_per"),
        migrations.RemoveField(
            model_name="energyscenario", name="share_RE_total_until"
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="emission_reductions_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="emission_reductions_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="potential_energy_savings_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="potential_energy_savings_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_heat_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_heat_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_mobility_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_mobility_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_power_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_power_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_total_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="until",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="share_RE_total_year",
            field=models.SmallIntegerField(default=2050),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="name_of_scenario",
            field=models.CharField(
                help_text="What is the name of the scenario?",
                max_length=100,
                unique=True,
                verbose_name="Name of the Scenario",
            ),
        ),
    ]
