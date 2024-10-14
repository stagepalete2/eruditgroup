from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'course_name', 'course_type', 'course_language', 'course_subcategory'
    ]
    prepopulated_fields = {'course_slug' : ['course_name']}

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name',
    ]


@admin.register(CourseSubcategory)
class CourseSubcategoryAdmin(admin.ModelAdmin):
    list_display = [
        'subcategory_name',
    ]

@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = [
        'type_name',
    ]
    
@admin.register(BannerImages)
class BannerImages(admin.ModelAdmin):
    list_display = [
        'image',
        'redirect_to'
    ]
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'banner_name',
        'banner_title',
    ]