# Generated by Django 4.2.5 on 2023-10-06 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0080_alter_register_info_weight_alter_vip_info_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 56, 45, 572680)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='ended_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 56, 45, 572680)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 56, 45, 572680)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 56, 45, 572680)),
        ),
    ]
