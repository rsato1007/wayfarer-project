# Generated by Django 3.2.8 on 2021-10-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_merge_20211023_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
