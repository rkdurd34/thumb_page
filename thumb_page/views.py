from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.
from thumb_page.models import *


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

def class_story(request):
    hooah = king_class.objects.all()

    return render(request, "thumb_page/class_story.html",{ "king_class": hooah })

def class_story_list(request,pk):
    certain_album = Album.objects.filter(pk=pk)

    return render(request, "thumb_page/class_story_list.html",{"certain_album" : certain_album})

def class_story_list_detail(request,pk):
    return render(request, "thumb_page/class_story_list_detail.html")


