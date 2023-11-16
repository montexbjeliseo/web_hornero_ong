from django import forms
from .models import *

class PostCommentForm(forms.ModelForm):
    
    class Meta:
        model = PostComment
        fields = ['text']