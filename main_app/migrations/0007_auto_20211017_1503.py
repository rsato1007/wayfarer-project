# Generated by Django 3.2.8 on 2021-10-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20211017_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'Cities'},
        ),
        migrations.RemoveField(
            model_name='city',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='London', max_length=50),
            preserve_default=False,
        ),
    ]
