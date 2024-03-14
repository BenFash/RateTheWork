from django.urls import path
from . import views
from .views import WorkDelete, CommentDelete, CommentEdit

urlpatterns = [
    path('', views.WorkList, name='work'),
    path('<int:pk>/', views.WorkDetail, name='work_detail'),
    path('delete/<int:pk>/', WorkDelete.as_view(), name='delete_work'),
    path('delete-comment/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),
    path('edit-comment/<int:pk>/', CommentEdit.as_view(), name='edit_comment'),    
    path('like/<int:pk>', views.WorkLike, name='work_like'),
]