from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.board.as_view()),
    path('<int:pk>/', views.detail.as_view()),
    path('', views.vie)
]
