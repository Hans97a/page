from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=10, blank=False)
    contact=models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
