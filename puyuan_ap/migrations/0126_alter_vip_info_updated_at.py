# Generated by Django 4.2.5 on 2023-10-09 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0125_rename_uid_friend_list_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 3, 15, 14, 834327)),
        ),
    ]
