from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    image=models.ImageField(verbose_name='프로필 이미지', blank=True, null=True, upload_to='profile/%Y/%m/%d')

    def __str__(self):
        return f'{self.nickname}'
