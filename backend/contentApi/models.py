from django.db import models
from userapi.models import User

# Create your models here.



class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=50,null=True,blank=True)

class Content(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30,null=True,blank=True)
    body=models.CharField(max_length=300,null=True,blank=True)
    summary=models.CharField(max_length=60,null=True,blank=True)
    document = models.FileField(upload_to='documents/')
    categories = models.ManyToManyField(Category, related_name='contents')
    
