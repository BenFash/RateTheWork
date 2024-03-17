from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView, name='profile'),
    path('upload_profile_pic/', views.UploadProfilePic, name='upload_profile_pic'),
    path('profile_comments/', views.ProfileComments, name='profile_comments'),
]