from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def forgotPassword(request):
    return render(request, "forgotPassword.html")

def signup(request):
    return render(request, 'signup.html')