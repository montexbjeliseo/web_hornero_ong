from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ['created_at', 'readed']