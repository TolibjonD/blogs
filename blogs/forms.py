from .models import Blogs
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','photo', 'blog_text')