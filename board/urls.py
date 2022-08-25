from django.contrib import admin
from django.urls import path, include
from . import views

app_name='board'

urlpatterns = [
    path('', views.board.as_view(), name='index'),
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    path('<int:pk>/comment/', views.comment, name='comment'),
    path('comment_update/<int:pk>', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment_delete/<int:pk>', views.comment_delete, name='delete'),
]