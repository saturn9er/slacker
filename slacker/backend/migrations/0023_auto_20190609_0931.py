# Generated by Django 2.2.1 on 2019-06-09 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_room_current_accommodation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='accomodation',
            new_name='accommodation',
        ),
    ]