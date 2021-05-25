from django.contrib import admin
from nextapp.models import AppDetail,UserDetail,AdminDetail,UserAppPic

# Register your models here.

admin.site.register(AppDetail)
admin.site.register(UserDetail)
admin.site.register(AdminDetail)
admin.site.register(UserAppPic)