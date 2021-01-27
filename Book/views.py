from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from Book.models import Book
# Create your views here.
def handle_signin(request):
    if request.method=='POST':
        try:
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('welcome')
            else:
                return redirect('home')
        except Exception as e:
            print(e)
            return redirect('home')
    else:
        pass
    return render(request,'home.html')


def handle_signup(request):
     if request.method=='POST':
        try:
             username = request.POST['username']
             password =request.POST['password']
             email =request.POST['email']
             newuser = User.objects.create_user(username=username,password=password,email=email)
             newuser.save()
             return redirect('home')

        except Exception as e:
            print(e)
     else:
         pass
     books=Book.objects.all()
     return render(request,'welcome.html',{'books':books})
        
def handle_logout(request):
    logout(request)
    return redirect('home')



                
           