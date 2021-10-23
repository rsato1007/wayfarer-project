from django.db import models
from django.contrib.auth.models import User
import time

# Pretty URLs using slugify
import string
import random

from django.utils.text import slugify

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_city = models.CharField(max_length=100)
    email = models.EmailField(max_length=500, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='profile/')
   
    def __str__(self):
        return str (self.user)


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True, upload_to='profile/')
    slug = models.SlugField(max_length=255, unique=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.name)
        super(City, self).save(*args, **kwargs)

    class Meta: 
        ordering = ['name']
        verbose_name_plural = "Cities"


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="post")
    image = models.FileField(blank=True, null=True, upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        
