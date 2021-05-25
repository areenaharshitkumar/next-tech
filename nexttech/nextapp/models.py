from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AppDetail(models.Model):
    app_name = models.CharField(max_length=250,blank=True)
    app_url = models.URLField(max_length=250,blank=True)
    app_category = models.CharField(max_length=250,blank=True)
    sub_category = models.CharField(max_length=250,blank=True)
    app_points = models.IntegerField(blank=True)
    app_pic = models.ImageField(upload_to='app_picture',blank=True)
    assigned_app = models.BooleanField(default=False)
    app_status = models.BooleanField(default=False)
    assigned_user = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.app_name

class AdminDetail(models.Model):
    admin_username = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=250)

    # def __str__(self):
    #     return self.user.username

class UserDetail(models.Model):
    user_username = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250,blank=True)
    email = models.EmailField(max_length=250,blank=True)
    mobile = models.CharField(max_length=250,blank=True)
    address = models.CharField(max_length=250,blank=True)
    user_type = models.CharField(max_length=250)
    assigned_app_id = models.IntegerField(blank=True)


    # def __str__(self):
    #     return self.user.username

class UserAppPic(models.Model):
    user_name = models.CharField(max_length=250,blank=True)
    app_pic = models.ImageField(upload_to='user_app_pic',blank=True)

    def __str__(self):
        return self.user_name