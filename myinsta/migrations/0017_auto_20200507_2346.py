# Generated by Django 3.0.4 on 2020-05-07 23:46

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myinsta', '0016_auto_20200507_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='{% media %}'),
        ),
    ]
