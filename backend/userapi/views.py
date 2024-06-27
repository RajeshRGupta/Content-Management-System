from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import generics,permissions


# Create your views here.


class RagisterView(APIView):
    template_name = 'rest_framework/api.html'
    def post(self,request,*args, **kwargs):
        try:
            context=request.data
            serializer=UserSerializer(data=request.data)
            # pdb.set_trace()
            if serializer.is_valid():
                user=serializer.save()
                print('ragister done')
                return Response({
                    'status':200,
                    'data':UserSerializer(user).data,
                    'massege':'ragister is successfull'
                })
            print('ragister fail')
            
            return Response({
                'status':403,
                'errors':serializer.errors
             })
            
        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'errors':'somthing went worng'
            })
            
            
            
class UserViewDU(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='id'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
