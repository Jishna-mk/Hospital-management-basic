from django.urls import path
from . import views

urlpatterns = [
    
    path('admin_page', views.admin_page, name='admin_page'),
    path('signin',views.admin_signin,name='admin_signin'),
    path('signout',views.admin_signout,name='admin_signout'),
    path('view_doctor',views.view_all_doctors, name='view_all_doctors')
]