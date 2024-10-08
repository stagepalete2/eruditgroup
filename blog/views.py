from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Article, ArticleCategory
# Create your views here.


class ArticlesPage(TemplateView):
    template_name = 'articles.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context.update({'Articles' : Article.objects.all()})
        
        
        
        return context
    
class ArticleDetailPage(DetailView):
    template_name = 'article.html'
    model = Article
    context_object_name = 'Article'
    slug_field = 'article_slug' 
    slug_url_kwarg = 'article_slug'
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset.order_by('-published')
        return queryset
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        return context