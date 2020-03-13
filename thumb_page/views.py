from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, "thumb_page/main_page.html")

def intro(request):
    return render(request,"thumb_page/intro.html")

def login(request):
    return render(request,"thumb_page/login.html")