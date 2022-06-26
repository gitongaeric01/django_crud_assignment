from django.shortcuts import render

# # Create your views here.
# import django
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post
import blog

class PostListView(ListView):
    model = Post
    # fields = '_all_'
    
    fields = [
        'title',
         'author',
        'body',
        'publish',
    ]

    template_name = 'blog/post_list.html'

class PostCreateView(CreateView):
    model = Post
    # fields = '_all_'
    fields = [
        'title',
         'author',
        'body',
        'publish',
 
    ]
    template_name = 'blog/post_form.html'
    success_url  = reverse_lazy('', PostListView.as_view())


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    # fields = '_all_'
    fields = [
        'title',
         'author',
        'body',
        'publish',
    
    ]

    template_name = 'blog/post_detail.html'
    success_url  = reverse_lazy('', PostListView.as_view())
    
class PostDeleteView(DeleteView):
    model = Post
    fields = '_all_'
    template_name = 'blog/post_confirm_delete.html'
    success_url  = reverse_lazy('', PostListView.as_view())
    