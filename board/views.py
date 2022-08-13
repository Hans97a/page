from django.shortcuts import render, HttpResponse
from .models import Post
from . import models, forms
from django.views.generic import ListView, DetailView
from django.db.models import Q
# Create your views here.

class board(ListView): # board 게시판의 메인 페이지
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ["-created_at"]
    
    
    def get_context_data(self, **kwargs):
        context = super(board, self).get_context_data(**kwargs)
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['pagelist'] = pagelist
        return context
    
    def get_queryset(self):
        keyword= self.request.GET.get('keyword', None)
        form = forms.SearchForm(self.request.GET)
        q=Q()
        filter_args={}

        if form.is_valid():
            if keyword is not None and keyword != "":
                q.add(
                    Q(title__icontains=keyword)
                    | Q(content__icontains=keyword),
                    q.OR
                )
                results=models.Post.objects.filter(q, **filter_args).order_by('-created_at')
            else:
                results=models.Post.objects.all().order_by('-created_at')
            return results


class detail(DetailView):
    model = Post
    template_name = 'board/detail.html'