from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import *


class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context = {
            'CourseCategories' : CourseCategory.objects.all(),
            'CourseSubcategories' : CourseSubcategory.objects.all(),
            'Courses' : Course.objects.all(), 
        }
        
        return context
    
class CatalogPage(ListView):
    template_name = 'courses.html'
    model = Course
    context_object_name = 'Courses'
    
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        # context = {
        #     'CourseCategories' : CourseCategory.objects.all(),
        #     'CourseSubcategories' : CourseSubcategory.objects.all(),
        #     'Courses' : Course.objects.all(), 
        # }
        
        return context
    
    
class CoursePage(DetailView):
    template_name = 'course.html'
    model = Course
    context_object_name = 'Course'
    slug_field = 'course_slug' 
    slug_url_kwarg = 'course_slug'
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset
    
# TODO: Update superclass from TemplateView to CreateView
class ScheduleConstructor(TemplateView):
    template_name = 'schedule.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        return context