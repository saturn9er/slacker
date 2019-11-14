# Generated by Django 2.1 on 2019-05-22 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20190519_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeddingConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capacity', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Occupancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_guests', models.PositiveSmallIntegerField(default=1)),
                ('check_in_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_out_at', models.DateTimeField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('paid', models.FloatField(blank=True, null=True)),
                ('payment_type', models.CharField(choices=[('CASH', 'Наличные'), ('BANK', 'Банковский перевод'), ('POS', 'Оплата картой')], default='CASH', max_length=4)),
            ],
        ),
        migrations.RenameField(
            model_name='room',
            old_name='type',
            new_name='room_type',
        ),
        migrations.RemoveField(
            model_name='room',
            name='configuration',
        ),
        migrations.AddField(
            model_name='roomnote',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='bedding_configuration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='backend.BeddingConfiguration'),
            preserve_default=False,
        ),
    ]
