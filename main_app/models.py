from django.db import models
from django.contrib.auth.models import User
import time

# Create "pretty" URLs 
from django.urls import reverse
from django.template.defaultfilters import slugify

def create_slug(name):
       slug = slugify(name)
       qs = City.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug
   
def create_slug(title): 
       slug = slugify(title)
       qs = Post.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug
   
def create_slug(post):
       slug = slugify(post)
       qs = Post.objects.filter(slug=slug)
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
        return self.user.username

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True, upload_to='city/')
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
      return reverse('city_detail', kwargs={'slug': self.slug})
  
    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = create_slug(self.name)
      return super().save(*args, **kwargs)

    
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
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
      return reverse('post_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = create_slug(self.title)
      return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.post
    
    def get_absolute_url(self):
      return reverse('post_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = create_slug(self.post)
      return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']