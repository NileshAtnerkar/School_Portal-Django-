
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"home.html")
def signup(request):


    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

    return render(request,"signup.html")
def signin(request):
    return render(request,"signin.html")
def signhome(request):
    return render(request,"signhome.html")
def about(request):
    return render(request,"about.html")
def noti(request):
    return render(request,"noti.html")

def gallery(request):
    return render(request,"gallery.html")
def contact(request):
    return render(request,"contact.html")


