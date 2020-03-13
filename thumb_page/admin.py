
from django.contrib import admin

from .models import *
from . import models




@admin.register(models.User)
class CustomerUserAdmin(admin.ModelAdmin):
    pass
