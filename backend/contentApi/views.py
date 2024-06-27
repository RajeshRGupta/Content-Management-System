from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import generics,permissions
from rest_framework.response  import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.




class ContentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    def perform_create(self, serializer):
        categories_data = self.request.data.pop('categories', [])
        content=serializer.save(user=self.request.user)
        content.categories.set(categories_data)


class ContentView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

        
class ContentUpdateDeletView(generics.DestroyAPIView,generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        

class ContentUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return Content.objects.filter(user=self.request.user)
        

        
class ContentUserUpdateDeletView(generics.DestroyAPIView,generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

