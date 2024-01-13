from django.shortcuts import render
from django.http import HttpResponse
from .models import NoticeBoard

# Create your views here.
def notices(request):
    notices = NoticeBoard.objects.order_by('-datetime')
    context = {'notices':notices, 'title':'College', 'site_name':'Notices'}
    return render(request, 'home.html', context)

def home(request):
    return render(request, 'demo.html')
