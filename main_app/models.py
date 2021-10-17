from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_city = models.CharField(max_length=100)
    
    def __str__(self):
        return str (self.user)

class City(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return str (self.city)
    
    class Meta: 
        ordering = ['city']

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post")
    # city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        
