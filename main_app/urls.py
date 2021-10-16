from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # Authentication routes
    path('registration/login/', views.Login.as_view(), name="login-user"), 
    path('registration/signup/', views.Signup.as_view(), name="signup"),
    # Profile routes
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile"),

    #City routes
    path('cities/', views.Cities.as_view(), name="cities"),
]