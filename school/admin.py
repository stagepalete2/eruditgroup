from django.contrib import admin
from .models import *
from .admin_models import CourseAdmin

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory)
admin.site.register(CourseSubcategory)
admin.site.register(CourseType)
admin.site.register(BannerImages)
admin.site.register(Banner)