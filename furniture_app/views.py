from django.shortcuts import render,redirect
from .models import Orders
import datetime as dt
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'project.html')

def featutes(request):
    return render(request,'feature.html')

def services(request):
    return render(request,'service.html')

def quotes(request):
    return render(request,"quote.html")

@login_required(login_url="login")
def booking(request):
        
        if request.method=="POST":
         username=request.POST['uname']
         useremail=request.POST['umail']
         contact=request.POST['mobile']
         uservice=request.POST['service']
         ubudget=request.POST['budget']
         unote=request.POST['note']

        #  print(username,useremail,contact,uservice,ubudget,unote)

         row=Orders.objects.create(name=username,email=useremail,mobile=contact,service=uservice,budget=ubudget,note=unote)
         row.save()

         bid=username[0:4]+"-wood-2025"
         date=dt.datetime.now()
         bdate=date.strftime("%d-%m-%y & %H:%M:%S")
         cname=username
         ccontact=contact
         cservice=uservice
         cbudget=ubudget
         cnote=unote
         pickup_date=date+dt.timedelta(days=7)
         pdate=pickup_date.strftime("%d-%m-%y")
         drop=pickup_date+dt.timedelta(days=15)
         ddate=drop.strftime("%d-%m-%y")

        
         data={"bid":bid,"bdate":bdate,"cname":cname,"cnumber":ccontact,
               "staken":cservice,"bvalue":cbudget,"snote":cnote,"pdate":pdate,"ddate":ddate}
        else:
            return render(request,"index.html")
        return render(request,"booking_info.html",data)


def teams(request):
    return render(request,'team.html')

def error(request):
    return render(request,'404.html')

def testimonials(request):
    return render(request,"testimonial.html")


def login_view(request):
    if request.method=="POST":
         user=authenticate(username=request.POST['username'],password=request.POST['password'])
         if user is not None:
             login(request,user)
             return redirect("home")
         else:
             messages.info(request,"Invalid Credentials")
             return render(request,"login.html")
    return render(request,"login.html")

def signup_view(request):
    if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm_password')

        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,"Account Already Exists !!!")
                return render(request,"signup.html")
            else:
                user=User.objects.create_user(username=name,password=password)
                login(request,user)
                messages.info(request,"Account Created Successfully")
                return redirect("home")
        else:
            messages.error(request,"Passwords Does not Match")

    return render(request,"signup.html")

def logout_view(request):
    logout(request)
    return redirect("login")    