# Generated by Django 3.0.4 on 2020-05-08 00:21

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myinsta', '0019_auto_20200508_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='photo/'),
        ),
    ]