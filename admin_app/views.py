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

