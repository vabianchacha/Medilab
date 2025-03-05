
from django.contrib import admin
from django.urls import path
from medapp import views

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
    path('login/', views.login_view, name='login'),



]
