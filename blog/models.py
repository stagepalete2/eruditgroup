from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class ArticleCategory(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

class Article(models.Model):
    article_title = models.CharField(max_length=255)
    article_small_description = models.CharField(max_length=255)
    article_author = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    article_image_public = models.ImageField(upload_to='blog/article_images/')
    tags = TaggableManager()
    article_slug = models.SlugField(default='', null=False)
    
    article_body = RichTextField()
    
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.id and not self.article_slug:
            self.article_slug = slugify(self.article_title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.article_title