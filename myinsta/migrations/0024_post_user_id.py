# Generated by Django 3.0.4 on 2020-05-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinsta', '0023_auto_20200508_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.TextField(blank=True),
        ),
    ]
