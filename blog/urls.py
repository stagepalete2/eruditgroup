from django.urls import path


from .views import ArticlesPage, ArticleDetailPage

urlpatterns = [
    path('articles/', ArticlesPage.as_view(), name='articles'),
    path('articles/<slug:article_slug>/', ArticleDetailPage.as_view(), name='article'),
] 