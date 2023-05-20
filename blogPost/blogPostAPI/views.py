from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from .models import BlogPost
from rest_framework import serializers, status
from rest_framework.views import APIView


# Create your views here.


class BlogPost(APIView):
    def get(self, request):
        items = BlogPost.objects.select_related('user').all()

        serialized_item = BlogPostSerializer(items, many = True)
        return Response(serialized_item.data, status = status.HTTP_200_OK)
    
        
    def post(self, request):
        serialized_item = BlogPostSerializer(data= request.data)
        serialized_item.is_valid(raise_exception= True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
    