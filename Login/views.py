from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request,'dashboardnexym.html')

def dashboardView(request):
    return render(request,'signup/signup.html')