# Generated by Django 3.2.8 on 2021-10-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(choices=[('LOS ANGELES, CA', 'LOS ANGELES, CA'), ('NEW YORK, NY', 'NEW YORK, NY'), ('WASHINGTON, D.C', 'WASHINGTON, D.C')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
