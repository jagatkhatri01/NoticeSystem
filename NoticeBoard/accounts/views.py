from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            user = User.objects.create(name=username, email=email, password=password1)
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('home')  # Redirect to the home page after registration
        except Exception as e:
            # Print the error and add an error message
            print(f"Error during user registration: {e}")
            messages.error(request, 'An error occurred during registration. Please try again.')

    return render(request, 'auth/register.html')    