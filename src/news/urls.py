from django.urls import path
from .views import AddArticleView, HomeView, ArticleView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('add_article/', AddArticleView.as_view(), name="add_article"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
]
