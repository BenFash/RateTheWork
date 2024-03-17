from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView, name='profile'),
    path('upload_profile_pic/', views.UploadProfilePic, name='upload_profile_pic'),
    path('profile_comments/', views.ProfileComments, name='profile_comments'),
    path('profile_posts/', views.ProfilePosts, name='profile_posts'),
    path('profile_likes/', views.ProfileLikes, name='profile_likes'),
]