# Generated by Django 4.2.4 on 2023-09-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0028_register_info_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
