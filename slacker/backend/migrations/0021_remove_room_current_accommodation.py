# Generated by Django 2.2.1 on 2019-06-09 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_room_current_accommodation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='current_accommodation',
        ),
    ]
