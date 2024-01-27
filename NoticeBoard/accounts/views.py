from django.shortcuts import render, redirect   
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        if not (username and password and password == confirm_password):
            messages.error(request, 'Invalid input')
            return render(request, 'auth/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use')
            return render(request, 'auth/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notices')
        else:
            messages.error(request, 'Invalid input')
    return render(request, 'auth/login.html')

@login_required
def profile_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'auth/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('notices')