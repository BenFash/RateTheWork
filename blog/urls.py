from django.urls import path
from . import views
from .views import WorkDelete, CommentDelete

urlpatterns = [
    path('', views.WorkList, name='post'),
    path('<int:pk>/', views.WorkDetail, name='work_detail'),
    path('delete/<int:pk>/', WorkDelete.as_view(), name='delete_work'),
    path('delete-comment/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),
    path('like/<int:pk>', views.WorkLike, name='work_like'),
]