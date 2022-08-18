from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True, verbose_name='닉네임')
    image = models.ImageField(
        verbose_name='프로필 이미지', blank=True, null=True, upload_to='profile/%Y/%m/%d')
    phone_number = models.CharField(max_length=11, verbose_name='휴대폰 번호')
    personal_id = models.CharField(max_length=15, verbose_name='아이디', unique=True)
    
    real_name = models.CharField(
        max_length=10, verbose_name='이름')
    def __str__(self):
        return f'{self.nickname}'
