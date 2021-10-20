
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Post, Profile, City

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'modal-form-input',}))
    email = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'modal-form-input',}))
    password1 = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'modal-form-input',}))
    password2 = forms.CharField(label="", help_text="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'modal-form-input',}))

    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']
      
class SignupForm(UserCreationForm):
    current_city = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'current_city', 'password1', 'password2',)
    
class LoginForm(ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'modal-form-input',}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'modal-form-input',}))

    class Meta:
        model = User
        fields = ('username', 'password1')

class ProfileForm(ModelForm):
    current_city = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'current_city')

class ProfilePictureForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('image',)
