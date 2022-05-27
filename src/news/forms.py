from django import forms
from .models import Comment, Post


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Article title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
        }