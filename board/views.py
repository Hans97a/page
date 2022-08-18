from django.shortcuts import render, HttpResponse
from .models import Post
from . import models, forms
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
# Create your views here.

class board(ListView): # board 게시판의 메인 페이지
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ["-created_at"]
    #paginate_queryset
    
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
        
        
    def paginate_queryset(self, queryset, page_size): #get_page / page

        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages # 마지막 페이지
            else:
                raise Http404(('Page is not “last”, nor can it be converted to an int.'))
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as e:
            raise Http404(('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })


class detail(DetailView):
    model = Post
    template_name = 'board/detail.html'