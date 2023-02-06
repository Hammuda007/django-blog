from django.shortcuts import render
from .models import Post

# Create your views here.


from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


class PostList(ListView):
    model=Post


class PostDetail(DetailView):
    model=Post



class PostCreate(CreateView):
    model=Post
    fields=['title','content','image']
    success_url='/blog'



class PostUpdate(UpdateView):
    model=Post
    fields=['title','content','image']
    success_url='/blog'




class PostDelete(DeleteView):
    model=Post
    success_url='/blog'




