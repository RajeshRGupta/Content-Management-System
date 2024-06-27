from django.urls import path
from .views import *

urlpatterns = [
    path('contentcreate/', ContentCreateView.as_view(), name ='contentcreate'),
    path('content/' , ContentView.as_view(),name='content'),
    path('contentupdatedelet/<pk>', ContentUpdateDeletView.as_view(), name ='contentupdatedelet'),
    path('contentuser/' , ContentUserView.as_view(),name='contentuser'),
    path('contentuserupdatedelet/<pk>', ContentUserUpdateDeletView.as_view(), name ='contentuserupdatedelet'),
]