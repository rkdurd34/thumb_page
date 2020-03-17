from django.contrib.auth.models import AbstractUser
from django.db import models
from mysite.utils import uuid_upload_to

# Create your models here.
class User(AbstractUser):

    GENDER_MALE  = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER,"Other")
    )
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10,blank=True,null=True)

class king_class(models.Model):
    name = models.CharField(max_length=10,blank=True,null=True)
    photo = models.ImageField(blank=True, null=True, upload_to=uuid_upload_to)

    def __str__(self):
        return self.name

class Album(models.Model):
    king_class=models.ForeignKey(king_class,on_delete=models.CASCADE, related_name='king_class', blank=True, null=True )
    title = models.CharField(max_length=100, blank=True,null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True,null=True)
    photo = models.ImageField(blank=True,null=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title






