from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Notice
from django.db.models import Q
from accounts.models import *
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model

def noticesView(request):
    query = request.GET.get('search')
    user = request.user
    
    dean_notices = Notice.objects.filter(author__role='dean').order_by('-datetime')

    if user.is_authenticated:
        department = user.department
        semester = user.semester
        user_notices = Notice.objects.filter(author__department=department, author__semester=semester).order_by('-datetime')
        notices = dean_notices | user_notices
    else:
        notices = dean_notices


    if query:
        # Filter notices based on search query
        notices = notices.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        )

    paginator = Paginator(notices, 6)
    page_num = request.GET.get("page", 1)  # Default to page 1 if no page is specified
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'notices': page_obj,  # Use the paginated queryset
        'title': 'College',
        'site_name': 'Notices',
        'page_obj': page_obj,
        'search_query': query
    }
    return render(request, 'home.html', context)




def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice_details.html', {'notice': notice})

@login_required
def add_notice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            if request.user.role in ['CR', 'dean']:  # Check if the user is CR or dean
                author = request.user
                notice = Notice.objects.create(title=title, content=content, author=author)
                return redirect('notices')
            else:
                return render(request, 'permission_denied.html')

    return render(request, 'add_notice.html')

@login_required
def update_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)

    if request.user.role in ['CR', 'dean'] and request.user == notice.author:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')

            if title and content:
                notice.title = title
                notice.content = content
                notice.save()
                return redirect('notices')

        return render(request, 'update_notice.html', {'notice': notice})
    else:
        return render(request, 'permission_denied.html')

@login_required
def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)

    if request.user.role in ['CR', 'dean'] and request.user == notice.author:
        if request.method == 'POST':
            notice.delete()
            return redirect('notices')
    else:
        return render(request, 'permission_denied.html')