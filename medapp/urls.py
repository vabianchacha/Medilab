
from django.contrib import admin
from django.urls import path
from medapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('stater/', views.stater, name='stater'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),


]
