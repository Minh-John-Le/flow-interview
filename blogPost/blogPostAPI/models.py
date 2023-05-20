from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class BlogPost(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now=True)

     def __str__(self) -> str:
          return self.title