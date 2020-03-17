from django.contrib import admin
from django.urls import path, include
from . import views

app_name  = 'thumb_page'

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path("intro/", views.intro, name='intro'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('intro_1/', views.intro_1, name="intro_1"),
    path('intro_2/', views.intro_2, name="intro_2"),
    path('class_story/', views.class_story, name="class_story"),
    path("class_story_list/<int:pk>", views.class_story_list, name="class_story_list"),

]