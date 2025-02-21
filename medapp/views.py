from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'index.html')
def stater(request):
    return render(request,'stater-page.html')