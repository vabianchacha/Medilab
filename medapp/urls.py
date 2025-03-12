import json

import requests
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from requests.auth import HTTPBasicAuth

from medapp import views
from medapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from medapp.models import Transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('stater/', views.stater, name='stater'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('appointment/', views.Appoint, name='appointment'),
    path('contact/', views.Contact, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit,name='edit'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),]


#Mpesa Api--------------

path('pay/', views.pay, name='pay'),
path('stk/', views.stk, name='stk'),
path('token/', views.token, name='token'),
path('transactions/', views.transactions_list, name='transactions'),