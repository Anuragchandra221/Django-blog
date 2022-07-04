from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from .models import Posts


# Create your views here.
def home(request):
    context = {
        'posts': Posts.objects.all(),
    }
    return render(request,'blog/index.html',context)

class PostListView(ListView):
    model = Posts
    template_name = "blog/index.html" # default -> app/model_viewtype.html
    context_object_name = 'posts' # default -> object 	
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Posts


class PostCreatView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content'] 
    # template default -> app/model_form.html

    success_url = "/"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content'] 
    # template default -> app/model_form.html

    success_url = "/"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'
    # template default -> app/model_confirm_delete.html
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})