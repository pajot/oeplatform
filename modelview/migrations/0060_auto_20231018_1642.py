# Generated by Django 3.2.22 on 2023-10-18 14:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("modelview", "0059_energyframework_link_to_installation_guide"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="energystudy",
            name="tools_models",
        ),
        migrations.DeleteModel(
            name="Energyscenario",
        ),
        migrations.DeleteModel(
            name="Energystudy",
        ),
    ]
