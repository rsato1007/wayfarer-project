from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_city = models.CharField(max_length=100)
    email = models.EmailField(max_length=500, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='profile/')
   
    
    def __str__(self):
        return self.user.username

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True, upload_to='city/')

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['name']
        verbose_name_plural = "Cities"

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="post")
    image = models.FileField(blank=True, null=True, upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']