from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.


class User(AbstractUser):
    username=None
    full_name=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=100)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name', 'phone']
    def name(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self):
        return self.email 


