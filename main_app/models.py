from django.db import models
from django.contrib.auth.models import User
import time

# Pretty URLS with Slug
from django.urls import reverse
from django.template.defaultfilters import slugify

def create_slug(name): # new
       slug = slugify(name)
       qs = City.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug

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
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
      return reverse('city_detail', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name)
      return super().save(*args, **kwargs)
  
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
        

class Comment(models.Model):
    parent_post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} made comment {self.title} on {self.created_date}'