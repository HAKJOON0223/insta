# Generated by Django 3.0.4 on 2020-04-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myinsta', '0012_auto_20200405_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_to_comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_comment', to='myinsta.Post'),
        ),
    ]