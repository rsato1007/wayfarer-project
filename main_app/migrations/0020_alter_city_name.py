# Generated by Django 3.2.8 on 2021-10-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_merge_0016_auto_20211020_0349_0018_auto_20211020_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
