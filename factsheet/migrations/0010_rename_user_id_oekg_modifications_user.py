# Generated by Django 3.2.7 on 2023-11-02 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factsheet', '0009_rename_user_oekg_modifications_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oekg_modifications',
            old_name='user_id',
            new_name='user',
        ),
    ]
