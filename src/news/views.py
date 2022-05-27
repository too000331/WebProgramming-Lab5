from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'


class AddArticleView(CreateView):
    model = Post
    form_class = ArticleForm
    template_name = 'add_article.html'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')