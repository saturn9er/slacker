# Generated by Django 2.1 on 2019-05-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20190522_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hourly_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]