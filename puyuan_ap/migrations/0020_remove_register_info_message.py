# Generated by Django 4.2.4 on 2023-09-20 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0019_alter_drug_used_info_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_info',
            name='message',
        ),
    ]
