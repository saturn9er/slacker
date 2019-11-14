# Generated by Django 2.2.1 on 2019-06-09 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_remove_room_current_accommodation'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='current_accommodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_accommodation', to='backend.Accommodation'),
        ),
    ]
