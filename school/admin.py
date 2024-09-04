from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CourseCategory)
admin.site.register(CourseSubcategory)
admin.site.register(CourseType)
admin.site.register(Course)
admin.site.register(BannerImages)
admin.site.register(Banner)