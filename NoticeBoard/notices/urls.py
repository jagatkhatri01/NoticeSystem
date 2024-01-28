from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', noticesView, name='notices'),
    path('notice/<int:notice_id>/', notice_detail, name='notice_detail'),
    path('add_notice/', add_notice, name='add_notice'),
    path('update_notice/<int:notice_id>/', update_notice, name='update_notice'),
   
]