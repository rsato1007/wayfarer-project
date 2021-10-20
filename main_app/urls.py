from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # Authentication routes
    path('registration/login/', views.Login.as_view(), name="login-user"), 
    path('registration/signup/', views.Signup.as_view(), name="signup"),
    # Profile routes
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    path('profile/<int:pk>/picture', views.ProfilePictureUpdate.as_view(), name="profile_picture_update"),
    # Post routes
    path('post/<int:pk>', views.PostDetail.as_view(), name="post_detail"),
    # City routes
    path('city/', views.CityList.as_view(), name="city_list"),
    path('city/<int:pk>', views.CityDetail.as_view(), name="city_detail"),
    path('city/post/new', views.Post_Create.as_view(), name="post_create"),
    path('city/post/<int:pk>/update', views.Post_Update.as_view(), name="post_update"),
    path('city/post/<int:pk>', views.Post_Detail.as_view(), name="post_detail"),
    path('city/post/<int:pk>/delete', views.Post_Delete.as_view(), name="post_delete"),
    # Comment routes
    path('comment/<int:pk>', views.Comment_Create.as_view(), name="comment_create"),
] 

