# Generated by Django 3.0.4 on 2020-04-05 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myinsta', '0011_comment_to_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='myinsta.Post'),
        ),
        migrations.AlterField(
            model_name='comment_to_comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_comment', to='myinsta.Comment'),
        ),
    ]
