# Generated by Django 3.2.8 on 2021-10-23 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_alter_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]