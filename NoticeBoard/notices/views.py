from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def notices(request):
    return HttpResponse('This is home page')

def home(request):
    return render(request, 'home.html')