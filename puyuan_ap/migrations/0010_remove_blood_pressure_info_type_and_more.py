# Generated by Django 4.2.4 on 2023-09-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0009_rename_user_id_blood_pressure_info_member_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_pressure_info',
            name='type',
        ),
        migrations.RemoveField(
            model_name='blood_sugar_info',
            name='type',
        ),
        migrations.RemoveField(
            model_name='body_weight_info',
            name='type',
        ),
        migrations.AddField(
            model_name='blood_sugar_info',
            name='drug',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='blood_sugar_info',
            name='exercise',
            field=models.IntegerField(null=True),
        ),
    ]
