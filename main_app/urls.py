from . import views 
from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit', views.PostEdit.as_view(), name="post_edit"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('post/<int:pk>/comments/new', views.CommentCreate.as_view(), name="comment_create"),
    path('category/hockey/', views.PostList.as_view(), name='hockey'),
    path('category/baseball/', views.PostList.as_view(), name='baseball'),
    path('category/basketball/', views.PostList.as_view(), name='basketball'),
    path('category/football/', views.PostList.as_view(), name='football'),
    path('category/soccer/', views.PostList.as_view(), name='soccer'),
]