# Generated by Django 3.1.6 on 2021-05-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextapp', '0002_admindetail_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAppPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=250)),
                ('app_pic', models.ImageField(blank=True, upload_to='user_app_pic')),
            ],
        ),
    ]
