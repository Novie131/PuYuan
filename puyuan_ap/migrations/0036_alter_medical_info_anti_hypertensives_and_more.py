# Generated by Django 4.2.4 on 2023-09-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0035_setting_info_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_info',
            name='anti_hypertensives',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='diabetes_type',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='insulin',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='oad',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
