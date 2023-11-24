# Generated by Django 4.2.5 on 2023-10-06 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0082_alter_vip_info_created_at_alter_vip_info_ended_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_info',
            name='gender',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 16, 12, 28, 979330)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='ended_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 16, 12, 28, 979330)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 16, 12, 28, 979330)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 16, 12, 28, 979330)),
        ),
    ]