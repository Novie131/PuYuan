# Generated by Django 4.2.5 on 2023-10-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0064_friends_requests_read_friends_requests_relation_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends_requests',
            name='created_at',
            field=models.DateTimeField(default='1920-1-1 00:00:00'),
        ),
        migrations.AddField(
            model_name='friends_requests',
            name='updated_at',
            field=models.DateTimeField(default='1920-1-1 00:00:00'),
        ),
    ]