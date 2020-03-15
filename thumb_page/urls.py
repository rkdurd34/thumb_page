from django.contrib import admin
from django.urls import path, include
from . import views

app_name  = 'thumb_page'

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path("intro/", views.intro, name='intro'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

]