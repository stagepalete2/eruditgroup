from django.urls import path

from .views import ArticlesPage, ArticleDetailPage

urlpatterns = [
    path('articles/', ArticlesPage.as_view(), name='articles'),
    path('article/', ArticleDetailPage.as_view(), name='article'),
]