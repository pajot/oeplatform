# Generated by Django 3.2.4 on 2023-01-20 14:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dataedit", "0020_peerreview"),
    ]

    operations = [
        migrations.RenameField(
            model_name="peerreview",
            old_name="in_progress",
            new_name="is_finished",
        ),
    ]
