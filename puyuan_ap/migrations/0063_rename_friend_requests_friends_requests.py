# Generated by Django 4.2.5 on 2023-10-04 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0062_rename_type_friend_list_relation_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='friend_requests',
            new_name='friends_requests',
        ),
    ]
