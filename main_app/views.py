from django.shortcuts import render, reverse
from django.views import generic
from .models import Post
from django.views.generic.edit import DeleteView, CreateView, UpdateView

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = '/'

class PostEdit(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_edit.html'
    def get_success_url(self):
         print(self.kwargs)
         return reverse('post_detail', kwargs={'pk': self.object.pk})
     
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'status', 'slug']
    template_name = "post_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        return reverse('post_detail', kwargs={'pk': self.object.pk})