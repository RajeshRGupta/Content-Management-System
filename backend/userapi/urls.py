from django.urls import path
from .views import *


urlpatterns = [
    path('ragister/' , RagisterView.as_view(),name='register'),
    path('userdatas/<id>', UserViewDU.as_view(), name ='userdata'),
]