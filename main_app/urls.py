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
    path('cities/', views.City.as_view(), name="city"),
   


    #City & Post routes

    path('cities/post/new', views.Post_Create.as_view(), name="post_create"),
    path('cities/post/<int:pk>/update', views.Post_Update.as_view(), name="post_update"),
    path('cities/post/<int:pk>', views.Post_Detail.as_view(), name="post_detail"),
    path('cities/post/<int:pk>/delete', views.Post_Delete.as_view(), name="post_delete"),
] 