
from django.contrib import admin

from .models import *
from . import models




@admin.register(models.User)
class CustomerUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album)
admin.site.register(Notice)
admin.site.register(king_class)