# Generated by Django 2.2.5 on 2019-10-28 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time, verbose_name='end time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time, verbose_name='start time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='event date'),
        ),
    ]