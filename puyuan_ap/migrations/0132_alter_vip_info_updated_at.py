# Generated by Django 4.2.5 on 2023-10-11 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0131_alter_a1c_info_created_at_alter_a1c_info_recorded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 11, 20, 48, 37, 432540)),
        ),
    ]