from django.db import models

# Create your models here.
class Page(models.Model):
    page_title = models.CharField(max_length=100)
    page_favicon = models.ImageField(upload_to='favicons')
    
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    
    # page_view = 