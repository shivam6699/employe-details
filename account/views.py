from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def index(request):
    return render(request,'index.html')



def signup(request):
    return render(request,'signup.html')


def signin(request):
    return render(request,'signin.html')

def signuppage(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        unm=request.POST['Username']
        pwd=request.POST['password']
        try:
            user=User.objects.get(username=unm)
            return render(request,'signup.html')
        except:
            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=unm,password=pwd)
            user.save()
            return render(request,'signin.html')
    else:
        return render (request,'signup.html')

def login(request):
    if (request.method== "POST"):
        unm=request.POST['unm']
        password=request.POST['password']
        user=auth.authenticate(username=unm,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'userhome.html')

        else:
            return render(request,'signin.html')
def userhome(request):
    return render(request,'userhome.html')

def logout(request):
    auth.logout(request)
    return render(request,'signup.html')



