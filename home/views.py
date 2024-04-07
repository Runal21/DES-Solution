from django.shortcuts import render,redirect
from  .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

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
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        location = request.POST.get('location')
        password = request.POST.get('password')
        
        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password,location=location)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        
        messages.success(request, 'Registration successful. You can now login.')
        return redirect('login')
    
    return render(request, 'home/register.html')


def loginpage(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    return render(request, 'home/login.html')

def logoutpage(request):
    logout(request)
    return render(request,'home/login.html')
