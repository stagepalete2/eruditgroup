from django.contrib import admin
from django.utils.text import slugify

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'news_slug' : ['title']}