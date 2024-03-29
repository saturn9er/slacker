# Generated by Django 2.2.1 on 2019-06-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_guest_home_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('NC', 'Непотверждено'), ('CO', 'Подтверждено'), ('CN', 'Отменено'), ('NS', 'Не прибытие'), ('CI', 'Заселен')], default='NC', max_length=2),
        ),
    ]
