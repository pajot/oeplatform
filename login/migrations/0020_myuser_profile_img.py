# Generated by Django 3.2.18 on 2023-03-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20201103_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='login/templates/images/'),
        ),
    ]
