from django.contrib import admin
from .models import *

# Register your models here.

class Categoryadmin(admin.ModelAdmin):
    list_display = ['user','category']

class Contentadmin(admin.ModelAdmin):
    list_display = ['user','title','body','summary','document']

admin.site.register(Category,Categoryadmin)
admin.site.register(Content,Contentadmin)
