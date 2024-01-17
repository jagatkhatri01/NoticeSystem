from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
from notices.urls import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = Student.objects.create(name=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('notices')
       
    return render(request, 'auth/register.html')    
