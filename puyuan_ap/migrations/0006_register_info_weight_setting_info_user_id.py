# Generated by Django 4.2.4 on 2023-09-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0005_a1c_info_blood_pressure_info_blood_sugar_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='weight',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='setting_info',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
