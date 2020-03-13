from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_page, name="main_page"),
    path("first/", views.intro, name='intro'),
    path('login/', views.login, name="login")


]