from django.contrib import admin
from .models import Article, ArticleCategory
# Register your models here.


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = [
        'article_title',
        'article_small_description',
        'article_author',
        'published',
        'modified'
    ]
    prepopulated_fields = {'article_slug': ['article_title']}
    
admin.site.register(ArticleCategory)