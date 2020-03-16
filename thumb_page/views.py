from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.
def main_page(request):
    return render(request, "thumb_page/main_page.html")

def intro(request):
    return render(request,"thumb_page/intro.html")

def login(request):
    return render(request,"thumb_page/login.html")

def logout(request):
    auth.logout(request)
    return redirect("thumb_page:login")
def intro_1(request):
    return render(request, "thumb_page/intro_1.html")
def intro_2(request):
    return render(request, "thumb_page/intro_2.html")

