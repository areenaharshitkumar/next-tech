from django.urls import path,include
from nextapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('adminpannel/',views.adminpannel,name='adminpannel'),
    path('userpannel/',views.userpannel,name='userpannel'),
    path('logout_admin/',views.logout_admin,name='logout_admin'),
    path('app_detail/<int:id>',views.AppDetailView.as_view()),
    path('user_detail/<int:id>',views.UserDetailView.as_view()),
    # path('app_detail/',views.AppDetailView.as_view()),
    path('api_auth',include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)