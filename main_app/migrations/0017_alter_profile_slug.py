# Generated by Django 3.2.8 on 2021-10-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
