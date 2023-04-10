from django.urls import path
from . import views

urlpatterns = [
    
    path('admin_page', views.admin_page, name='admin_page'),
    path('signin',views.admin_signin,name='admin_signin'),
    path('signout',views.admin_signout,name='admin_signout'),
    path('view_doctor',views.view_all_doctors, name='view_all_doctors'),
    path('view_user',views.view_user_profile,name=' view_user_profile'),
    path('view_booking',views.view_bookings,name='view_bookings'),
    # path('delete_booking/<int:aid>',views.delete_booking,name='delete_booking')
]