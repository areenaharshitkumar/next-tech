from rest_framework import serializers
from nextapp.models import AppDetail,UserDetail


class AppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDetail
        fields = ('id','app_name','app_category','app_points')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__' #('id','app_name','app_category','app_points')