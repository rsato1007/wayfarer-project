from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('registration/signup/', views.Signup.as_view(), name="signup"),
    path('profile', views.ProfilePage.as_view(  ), name="profile"),
]