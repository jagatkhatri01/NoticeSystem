from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Notice
from django.db.models import Q
from accounts.models import *
from django.contrib.auth.decorators import user_passes_test, login_required


def noticesView(request):
    query = request.GET.get('search')
    notices = Notice.objects.order_by('-datetime')

    if query:
        # Filter notices based on search query
        notices = notices.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        )

    paginator = Paginator(notices, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    context = {'notices':notices,
                'title':'College',
                'site_name':'Notices',
                'page_obj':page_obj,
                'search_query':query
                }
    return render(request, 'home.html', context)


def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice_details.html', {'notice': notice})

@login_required
def add_notice(request):
    if request.user.role == 'CR':
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')

            if title and content:
                author = request.user
                notice = Notice.objects.create(title=title, content=content, author=author)
                return redirect('notices')

        return render(request, 'add_notice.html')
    else:
        return render(request, 'permission_denied.html') 


@login_required
def update_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)

    if request.user.role == 'CR' and request.user == notice.author:
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