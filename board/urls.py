from django.contrib import admin
from django.urls import path, include
from . import views

app_name='board'

urlpatterns = [
    path('', views.board.as_view(), name='index'),
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    path('<int:pk>/comment/', views.comment, name='comment'),
]