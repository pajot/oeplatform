# Generated by Django 3.2.13 on 2023-03-08 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dataedit', '0021_rename_in_progress_peerreview_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='peerreview',
            name='dateStarted',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=1000),
        ),
    ]
