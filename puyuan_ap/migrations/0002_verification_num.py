# Generated by Django 4.2.4 on 2023-09-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='verification_num',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
