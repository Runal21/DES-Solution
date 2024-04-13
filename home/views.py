from django.shortcuts import render,redirect
from  .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from home.models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        location =request.POST.get("location")
        password = request.POST.get('password')
        
        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
        
        # Create the user
        # user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email,password=password)
        user = CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email,location=location,password=password)
        user.save()
        
        messages.success(request, 'Registration successful. You can now login.')
        return redirect('login')
    
    return render(request, 'home/register.html')


def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    return render(request, 'home/login.html')

def logoutpage(request):
    logout(request)
    return render(request,'home/login.html')
