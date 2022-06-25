# from django.shortcuts import render

# # Create your views here.
# import django
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    fields = '_all_'
    template_name = 'blog/post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = '_all_'
    # fields = [
    #     'title',
    #      'author',
    #     'body'
    # ]
    template_name = 'blog/post_form.html'
    # success_url  = reverse_lazy(“blog:all”)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = '_all_'
    template_name = 'blog/post_detail.html'
    # success_url  = reverse_lazy(“blog:all”)
    
class PostDeleteView(DeleteView):
    model = Post
    fields = '_all_'
    template_name = 'blog/post_confirm_delete.html'
    # success_url  = reverse_lazy(“blog:all”)
    