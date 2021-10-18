
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']
      
class SignupForm(UserCreationForm):
    current_city = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'current_city', 'password1', 'password2',)

class ProfileForm(ModelForm):
    current_city = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'current_city')