from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkList, name='work'),
    path('<int:pk>/', views.WorkDetail, name='work_detail'),
    path('new', views.CreateWork, name='new_work'),
    path('delete/<int:pk>/', views.WorkDelete, name='delete_work'),
    path('edit/<int:pk>/', views.WorkEdit, name='edit_work'),
    path('delete-comment/<int:pk>/', views.CommentDelete.as_view(), name='delete_comment'),
    path('edit-comment/<int:pk>/', views.CommentEdit.as_view(), name='edit_comment'),    
    path('like/<int:pk>', views.WorkLike.as_view(), name='work_like'),
]