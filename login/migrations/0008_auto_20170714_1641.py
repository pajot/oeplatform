# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-14 14:41
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("login", "0007_myuser_groups")]

    operations = [
        migrations.CreateModel(
            name="GroupMembership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "level",
                    models.IntegerField(
                        choices=[
                            (0, "None"),
                            (4, "Invite"),
                            (8, "Remove"),
                            (12, "Admin"),
                        ],
                        default=4,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="login.UserGroup",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="myuser", name="groups"),
        migrations.AddField(
            model_name="groupmembership",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberships",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
