from django.urls import path
from . import views
from .views import WorkDelete, WorkEdit, CommentDelete, CommentEdit, CreateWork

urlpatterns = [
    path('', views.WorkList, name='work'),
    path('<int:pk>/', views.WorkDetail, name='work_detail'),
    path('new', views.CreateWork, name='new_work'),
    path('delete/<int:pk>/', WorkDelete.as_view(), name='delete_work'),
    path('edit/<int:pk>/', WorkEdit.as_view(), name='edit_work'),
    path('delete-comment/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),
    path('edit-comment/<int:pk>/', CommentEdit.as_view(), name='edit_comment'),    
    path('like/<int:pk>', views.WorkLike, name='work_like'),
]