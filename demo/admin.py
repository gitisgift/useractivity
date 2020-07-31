from django.contrib import admin

# Register your models here.
from .models import UserInfo,UserTime

admin.site.register(UserTime)
admin.site.register(UserInfo)
