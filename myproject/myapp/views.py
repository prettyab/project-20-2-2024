from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('Fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        department = request.POST.get('department')
        year_of_experience = request.POST.get('yearofExperience')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.username =email
        user.save()

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('user_login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email,password=password)
        if user is not None:
            auth_login(request, user)

            request.session['user_id'] = user.id
            request.session['user_email'] = user.email

            return redirect('home2')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('user_login')

    return render(request, 'loggin.html')

def home2(request):
    return render(request, 'home2.html')

def homee(request):
    return render(request, 'homee.html')