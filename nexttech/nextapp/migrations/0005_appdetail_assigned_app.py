# Generated by Django 3.1.6 on 2021-05-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextapp', '0004_userdetail_assigned_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appdetail',
            name='assigned_app',
            field=models.BooleanField(default=False),
        ),
    ]
