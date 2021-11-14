from . import views 
from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit', views.PostEdit.as_view(), name="post_edit"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('hockey/', views.HockeyList.as_view(), name='hockey'),
    path('basketball/', views.BasketballList.as_view(), name='basketball'),
    path('baseball/', views.BaseballList.as_view(), name='baseball'),
    path('football/', views.FootballList.as_view(), name='football'),
    path('soccer/', views.SoccerList.as_view(), name='soccer'),
    path('category/<str:cats>/', CategoryView, name='category'),
]