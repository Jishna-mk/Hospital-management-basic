from django.shortcuts import render,redirect
from django.http import HttpResponse
from email import message

from django.contrib.auth.models import User
from admin_app.forms import  UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from users.models import UserProfile
from users.models import Booking
from doctors.models import DoctorProfile

# Create your views here.


# def admin_page(request):
#     return HttpResponse("Hello world!")

def admin_page(request):
    user_count=UserProfile.objects.count()
    doctor_count=DoctorProfile.objects.count()
    booking_count=Booking.objects.count()
    return render(request,"admin/admin.html",{"user_count":user_count,"doc_count": doctor_count,"bookings":booking_count})




def admin_signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("admin_page")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"admin/admin_signin.html")

def admin_signout(request):

    logout(request)
    return redirect("admin_signin")    

def view_all_doctors(request):
    all_doctors = DoctorProfile.objects.all()
    doctor_count = all_doctors.count()
    return render(request,"admin/doctors_view.html",{"all_doctors":all_doctors,"doctor_count":doctor_count})

# def view_user_profile(request):
#     user = UserProfile.objects.filter(user_ID=request.user.id)
#     if(len(user) == 0):
#         return redirect("add_user_profile")
#     return render(request,"users/user-profile.html",{"user":user[0]})

def view_user_profile(request):
    all_users = UserProfile.objects.all()
    user_count=all_users.count()
    return render(request,"admin/users_view.html",{"all_users": all_users,"user_count":user_count })

# def view_my_bookings(request):
#     all_bookings = Booking.objects.filter(Patient_ID=request.user.id).exclude(status="Cancelled").exclude(status="Cancelled By Doctor")
#     app_count = all_bookings.count()
#     return render(request,"users/view-all-bookings.html",{"all_bookings":all_bookings,"app_count":app_count})

def view_bookings(request):
    all_bookings = Booking.objects.all()
    app_count = all_bookings.count()
    return render(request,"admin/view_bookings.html",{"all_bookings":all_bookings,"app_count":app_count})

# def delete_booking(request,pk):
#       b= Booking.objects.get(pk=pk)
#       b.delete()
#       messages.info(request,"successfully deleted")
#       return redirect("admin_page")
  
  
def delete_booking(request):

    bookings = Booking.objects.all()
    if request.method == "POST":
        id = request.POST["id"]
        booking= Booking.objects.get(Patient_ID =id)
        booking.delete()
        messages.info(request, "booking Deleted!")
        return redirect("delete_booking")

    return render(request, "admin/admin.html", {"bookings": bookings})