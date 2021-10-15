from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    current_city = models.CharField(max_length=100)
    joined = models.DateField(max_length=100)
    
    def __str__(self):
        return str (self.user)