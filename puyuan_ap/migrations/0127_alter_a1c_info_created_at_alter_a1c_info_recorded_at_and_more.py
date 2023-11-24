# Generated by Django 4.2.5 on 2023-10-10 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0126_alter_vip_info_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a1c_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='blood_pressure_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='blood_sugar_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='body_weight_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='default_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='default_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='diet_diary_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='drug_used_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='friends_requests',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='friends_requests',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='message_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='message_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='pushed_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='ended_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='started_at',
            field=models.DateTimeField(default='2023-10-10 15'),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 15, 33, 26, 681197)),
        ),
    ]
