# Generated by Django 2.2.8 on 2022-04-21 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0009_delete_reviewsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptour',
            name='date_submitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deptour',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Desired Date and Time'),
        ),
    ]
