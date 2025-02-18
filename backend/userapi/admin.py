from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email','full_name','phone','address','city','state','pincode','country',]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'address','phone','city','state','pincode','country',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email', 'full_name', 'address','phone','city','state','pincode','country',)

admin.site.register(User, UserAdmin)
