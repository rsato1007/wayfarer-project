# Generated by Django 3.2.8 on 2021-10-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_comment_parent_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
