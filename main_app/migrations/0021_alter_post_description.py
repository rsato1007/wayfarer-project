# Generated by Django 3.2.8 on 2021-10-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]