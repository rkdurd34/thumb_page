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


class Album(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True,null=True)
    photo = models.ImageField(blank=True,null=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notice(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






