# Generated by Django 3.2.8 on 2021-10-27 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
