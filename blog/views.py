from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class ArticlesPage(TemplateView):
    template_name = 'articles.html'
    
    
class ArticleDetailPage(TemplateView):
    template_name = 'article.html'