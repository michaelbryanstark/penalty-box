from django.shortcuts import render, reverse
from django.views import generic
from .models import Post, Categories
from django.views.generic.edit import DeleteView, CreateView, UpdateView

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # cats = Categories.objects.all()
    
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Categories.objects.all()
    #     context = super(PostList, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = '/'

class PostEdit(UpdateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'post_edit.html'
    def get_success_url(self):
         print(self.kwargs)
         return reverse('post_detail', kwargs={'pk': self.object.pk})
     
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'status', 'slug', 'category']
    template_name = "post_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts':category_posts})
    
class HockeyList(generic.ListView):
    model = Post
    template_name = 'hockey.html'
    
class BasketballList(generic.ListView):
    model = Post
    template_name = 'basketball.html'
    
class BaseballList(generic.ListView):
    model = Post
    template_name = 'baseball.html'
    
class FootballList(generic.ListView):
    model = Post
    template_name = 'football.html'
    
class SoccerList(generic.ListView):
    model = Post
    template_name = 'soccer.html'
    
