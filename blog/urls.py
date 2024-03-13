from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_list, name='post'),
    path('<int:pk>/', views.work_detail, name='work_detail'),
    path('like/<int:pk>', views.work_like, name='work_like'),
]