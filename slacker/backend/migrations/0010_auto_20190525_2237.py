# Generated by Django 2.2.1 on 2019-05-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_documenttype_guest_guestimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttype',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]