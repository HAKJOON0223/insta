# Generated by Django 3.0.4 on 2020-05-06 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_profile_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
