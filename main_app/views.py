from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth import login
from .models import Post, Comment, User
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm

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
    form_class = PostForm
    # fields = ['title', 'content', 'category']
    template_name = 'post_edit.html'
    def get_success_url(self):
         print(self.kwargs)
         return reverse('post_detail', kwargs={'pk': self.object.pk})
     
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'author', 'status', 'slug', 'category']
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
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
    
class CommentCreate(View):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        name = request.POST.get("name")
        description = request.POST.get("description")
        Comment.objects.create(post=post, name=name, description=description)
        return redirect('post_detail', pk=pk)
    # def post(self, request, pk):
    #     name = request.POST.get("name")
    #     body = request.POST.get("body")
    #     post = Post.objects.get(pk=pk)
    #     Comment.objects.create(name=name, body=body, post=post)
    #     return redirect('post_detail', pk=pk)
 