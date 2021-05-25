from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, response
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from nextapp.models import AppDetail,UserDetail,AdminDetail, UserAppPic
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework  import status , permissions
from rest_framework.views import APIView
from nextapp.serializers import AppDetailSerializer, UserDetailSerializer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class IsReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow read-only operations.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

class AppDetailView(APIView):

    permission_classes = (IsReadOnly,)

    def get(self,request,id):
        try:
            appdetail = AppDetail.objects.get(id=id)
            sr = AppDetailSerializer(appdetail)
            return Response(sr.data)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        sr = AppDetailSerializer(data=request.data)

        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_201_CREATED)
        return Response(sr.error, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):

    permission_classes = (IsReadOnly,)

    def get(self,request,id):
        try:
            userdetail = UserDetail.objects.get(id=id)
            sr = UserDetailSerializer(userdetail)
            return Response(sr.data)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        sr = UserDetailSerializer(data=request.data)

        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_201_CREATED)
        return Response(sr.error, status=status.HTTP_400_BAD_REQUEST)




@login_required
def logout_admin(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def index(request):
    if request.method == 'POST':
        if request.POST.get('hidden') == 'admindetail':
            user = User()
            admin_deatil = AdminDetail()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.save()
            user.set_password(user.password)
            user.save()

            
            admin_deatil.admin_username  = user
            admin_deatil.user_type = 'admin'
            admin_deatil.save()
        elif request.POST.get('hidden') == 'userdetail':
            user = User()
            user_deatil = UserDetail()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.email = request.POST.get('email')
            user.save()
            user.set_password(user.password)
            user.save()
            
            user_deatil.user_username  = user
            user_deatil.full_name = request.POST.get('fullname')
            user_deatil.email = request.POST.get('email')
            user_deatil.mobile = request.POST.get('mobile')
            user_deatil.address = request.POST.get('address')
            user_deatil.user_type = 'user'
            user_deatil.save()
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if request.POST.get('hidden') == 'adminlogin':
                user = authenticate(username=username,password=password)

                if user:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('adminpannel'))
                    else:
                        return HttpResponse('Account is not active')
                else:
                    return HttpResponse('Invalid login details')
            else:
                user = authenticate(username=username,password=password)

                if user:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('userpannel'))
                    else:
                        return HttpResponse('Account is not active')
                else:
                    return HttpResponse('Invalid login details')
    return render(
        request,
        'index.html',
        {
            'title':'Login Pannel',
        }
    )

@login_required
def adminpannel(request):
    if request.method == 'POST':
        try:
            if request.POST.get('hidden') == 'app_detail':
                ad = AppDetail()
                ad.app_name = request.POST.get('appname')
                ad.app_url = request.POST.get('applink')
                ad.app_category = request.POST.get('appcategory')
                ad.sub_category = request.POST.get('subcategory')
                ad.app_points = int(request.POST.get('apppoints'))
                ad.app_pic = request.FILES['apppicture']
                ad.save()
            elif request.POST.get('hidden') == 'taskassign':
                # print(str(request.POST.get('taskassign')).split('_'))
                user_info = UserDetail.objects.get(email=str(request.POST.get('taskassign')).split('_')[1])
                user_info.assigned_app_id = int(str(request.POST.get('taskassign')).split('_')[0])
                user_info.save()
                ad = AppDetail.objects.get(id=int(str(request.POST.get('taskassign')).split('_')[0]))
                ad.assigned_app = True
                ad.assigned_user = user_info.user_username.username
                ad.save()
                # pass
            else:
                AppDetail.objects.filter(id=int(request.POST.get('hidden'))).delete()

        except Exception as e:
            print(e)
    ad = AppDetail.objects.all()
    user = UserDetail.objects.all()
    return render(
        request,
        'admin.html',
        {
            'title':'Admin Pannel',
            'app_detail':ad,
            'user':user,
        }
    )

@login_required
def userpannel(request):
    if request.method == 'POST':
        try:
            if request.POST.get('hidden') == 'editdetail':
                user_info = UserDetail.objects.get(email=request.user.email)
                
                user_info.full_name = request.POST.get('fullname')
                user_info.mobile = request.POST.get('mobile')
                user_info.address = request.POST.get('address')
                user_info.save()
            else:
                uap = UserAppPic()
                uap.user_name = request.user.username
                uap.app_pic = request.FILES['file']
                uap.save()

                ad = AppDetail.objects.get(assigned_user=request.user.username)
                ad.app_status = True
                ad.save()

        except Exception as e:
            pass
    ad = ''
    user_info =''
    try:
        # ad = AppDetail.objects.all()
        ad = AppDetail.objects.filter(assigned_user=request.user.username,app_status=False)
        user_info = UserDetail.objects.filter(email=request.user.email)[0]
        points = AppDetail.objects.filter(assigned_user=request.user.username,app_status=True)
    except Exception as e:
        pass
    return render(
        request,
        'userpannel.html',
        {
            'title':'User Pannel',
            'app_detail':ad[:],
            'user_detail':user_info,
            'points':points,
        }
    )
