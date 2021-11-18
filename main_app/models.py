from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Categories(models.TextChoices):
    HOCKEY = 'hockey'
    BASEBALL = 'baseball'
    BASKETBALL = 'basketball'
    FOOTBALL = 'football'
    SOCCER = 'soccer'

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.HOCKEY)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
