from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'index.html')
def stater(request):
    return render(request,'starter-page.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')