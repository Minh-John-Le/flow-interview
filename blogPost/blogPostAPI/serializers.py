from rest_framework import serializers
from decimal import Decimal
from django.contrib.auth.models import User
from.models import BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'username']

class BlogPostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = True)
    user_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'user', 'create_at','user_id']
