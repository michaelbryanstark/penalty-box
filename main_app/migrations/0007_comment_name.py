# Generated by Django 3.2.7 on 2021-11-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
