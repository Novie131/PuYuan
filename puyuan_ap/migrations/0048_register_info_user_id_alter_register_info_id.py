# Generated by Django 4.2.4 on 2023-09-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0047_alter_register_info_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='user_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='register_info',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]