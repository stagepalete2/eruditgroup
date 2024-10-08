from django.contrib import admin
from .models import Article, ArticleCategory
from .admin_models import AdminArticle
# Register your models here.


admin.site.register(Article, AdminArticle)
admin.site.register(ArticleCategory)