from django.db import models
# from users.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}] -- {self.title}'

    def get_absolute_url(self):
        return f'{self.pk}'


class PostImage(models.Model):
    post=models.ForeignKey('board.Post', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/%Y/%m/%d')