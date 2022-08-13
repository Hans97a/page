from django.contrib import admin
from .models import Post, PostImage
# Register your models here.


class PostImageInline(admin.StackedInline):
    model=PostImage
    extra=1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines=[PostImageInline]
