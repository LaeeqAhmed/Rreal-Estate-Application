from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your accounts views here.
#messages.error(request,'testing error message')

def register(request):
    # check if the request is post or get
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request,'User already exist in database')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email already exist in database')
            return redirect('register')
        elif password != password2:
            messages.error(request,'passwords do not match')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,'You are now Registered and can login')
            return redirect('login')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        # check if user credentials are valid or not
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
