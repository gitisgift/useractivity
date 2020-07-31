# Generated by Django 3.0.8 on 2020-07-31 08:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200731_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertime',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 8, 42, 35, 338463, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activity_periods', to='demo.UserInfo'),
        ),
    ]
