# Generated by Django 4.2.5 on 2023-10-11 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0128_delete_friend_list_alter_a1c_info_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends_requests',
            old_name='type',
            new_name='relation_type',
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 11, 17, 4, 52, 973729)),
        ),
    ]