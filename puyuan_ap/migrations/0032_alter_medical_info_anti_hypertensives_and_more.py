# Generated by Django 4.2.4 on 2023-09-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0031_message_info_delete_message_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_info',
            name='anti_hypertensives',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='insulin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='oad',
            field=models.IntegerField(null=True),
        ),
    ]