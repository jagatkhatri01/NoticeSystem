from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def notices(request):
    context = {'title':'College', 'site_name':'Notices'}
    return render(request, 'home.html', context)

