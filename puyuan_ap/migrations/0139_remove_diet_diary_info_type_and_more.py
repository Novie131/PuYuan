# Generated by Django 4.2.5 on 2023-10-17 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0138_alter_a1c_info_created_at_alter_a1c_info_recorded_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet_diary_info',
            name='type',
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='blood_pressure_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='blood_sugar_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='body_weight_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='default_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='default_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='diet_diary_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='drug_used_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='friends_requests',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='friends_requests',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='message_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='message_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='pushed_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-17 20:04:59'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='ended_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='started_at',
            field=models.DateTimeField(default='2023-10-17 20'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 20, 4, 59, 651949)),
        ),
    ]
