# Generated by Django 3.2.8 on 2021-10-23 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_date',
            new_name='created_date',
        ),
    ]
