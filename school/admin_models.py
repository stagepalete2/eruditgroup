from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'course_slug' : ['course_name']}