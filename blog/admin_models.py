from django.contrib import admin
from .models import Article


class AdminArticle(admin.ModelAdmin):
    prepopulated_fields = {'article_slug': ['article_title']}