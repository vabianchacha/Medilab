from django.shortcuts import render, redirect, get_object_or_404
from medapp.models import *

# Create your views here.
def home(request):
    return render(request,'index.html')
def stater(request):
    return render(request,'starter-page.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')

def Appoint(request):
    if request.method=='POST':
        myappointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            doctor=request.POST['doctor'],
            department=request.POST['department'],
            message=request.POST['message'],

        )
        myappointments.save()
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')

def Contact(request):
    if request.method=='POST':
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )

def show(request):
    all = Appointment.objects.all()
    return render(request,'show.html',{'all':all})


def delete(request,id):
    deleteappointment = Appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show')

def edit(request,id):
    appointment = get_object_or_404 (Appointment,id=id)
    if request.method == 'POST':
        appointment.name = request.POST.get('name')
        appointment.email = request.POST.get('email')
        appointment.phone = request.POST.get('phone')
        appointment.date = request.POST.get('date')
        appointment.doctor = request.POST.get('doctor')
        appointment.department = request.POST.get('department')
        appointment.message = request.POST.get('message')
        appointment.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'appointment': appointment})

def register(request):
    return render(request,'register.html')


def login_view (request):
    return render(request, 'login.html')