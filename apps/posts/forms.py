from django import forms
from .models import *

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ['created_at', 'updated_at', 'likes', 'author', 'views']

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'