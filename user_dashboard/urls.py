from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView, name='profile'),
    path('upload_profile_pic/', views.UploadProfilePic, name='upload_profile_pic'),
]