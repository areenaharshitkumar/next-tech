# Generated by Django 3.1.6 on 2021-05-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextapp', '0003_userapppic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='assigned_app_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
