# Generated by Django 4.2.5 on 2023-10-04 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0066_remove_default_info_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='default_info',
            name='name',
        ),
    ]