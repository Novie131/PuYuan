# Generated by Django 4.2.4 on 2023-09-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0029_register_info_state_alter_register_info_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='must_change_password',
            field=models.IntegerField(default=0),
        ),
    ]
