from django.shortcuts import render, HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

# def board(request):
#     posts=Post.objects.all().order_by('-pk')
#     return render(request, 'board/index.html', {'posts': posts})


# def detail(request, pk):
#     post=Post.objects.get(pk=pk)
#     return render(request, 'board/detail.html', {'post': post})

class board(ListView):
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ["-created_at"]


class detail(DetailView):
    model = Post
    template_name = 'board/detail.html'
