# Generated by Django 4.2.5 on 2023-09-27 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0059_alter_register_info_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_info',
            name='user_id',
        ),
    ]
