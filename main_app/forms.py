from django import forms
from .models import Post, User, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['excerpt']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        
class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  username = forms.EmailField()

  class Meta:
    model = User
    fields =['username','password']
    
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'body']
        
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#         }