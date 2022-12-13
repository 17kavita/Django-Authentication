from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django .contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        fname=request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user=User.objects.create_user(username,email,password)
        new_user.first_name=fname
        new_user.last_name=lname
        new_user.save()
        return redirect('login')

    return render(request,'register.html')


def Login(request):

    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('password')

        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('error,user does not exist')



    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')
