from rest_framework import serializers
from decimal import Decimal
from django.contrib.auth.models import User
from.models import BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BlogPostSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only = True)
    author_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'created_at','author_id' , 'author', 'content']
