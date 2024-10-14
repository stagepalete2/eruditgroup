from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import *
from blog.models import Article
from eruditplatform.models import GroupCourse


class HomePage(TemplateView):
    template_name = 'home.html'
    
    
    def create_menu_items(self):
        MenuItems = []
        
        categories = CourseCategory.objects.all()
        subcategories = CourseSubcategory.objects.all()

        # Iterate over each category
        for category in categories:
            # Get all subcategories that belong to the current category
            category_subcategories = subcategories.filter(course_category=category)
            
            # Create a list of subcategories for this category
            subcategory_list = [{'subcategory_name': subcategory.subcategory_name} for subcategory in category_subcategories]
            
            # Append the category and its subcategories to MenuItems
            MenuItems.append({
                'category_name': category.category_name,
                'categories': subcategory_list  # This is the list of subcategories
            })
        
        return MenuItems
        
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        
        MenuItems = self.create_menu_items()
        
        context.update(
            MenuItems = MenuItems,
            CourseSubcategories = CourseSubcategory.objects.all(),
        )
        
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
    
    
    def post(self, request, *args, **kwargs):
        ...
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        FORMAT = {'offline' : 'Офлайн', 'online' : 'Онлайн'}
        GROUP_TYPE = {'individual' : 'Индивидуально', 'group': 'В группе'}
        LESSON_DURATION = {'45' : '45 Минут', '60' : ' 60 Минут', '90' : '90 Минут'}
        LESSON_LANG = {'rus' : 'Русский', 'kaz' : 'Казахский'}
        
        lesson_format = self.request.GET.get('lesson-format-outlined')
        group_type = self.request.GET.get('group-type-outlines')
        lesson_duration = self.request.GET.get('duration-outlines')
        lesson_lang = self.request.GET.get('lesson-lang-outlined')
        
        
        
        context.update(
            lesson_format = FORMAT[lesson_format],
            group_type = GROUP_TYPE[group_type],
            lesson_duration = LESSON_DURATION[lesson_duration],
            lesson_lang = LESSON_LANG[lesson_lang],
        )
        
        return context
    


def search_input(request):
    q = request.GET.get('q', '')

    articles = list(Article.objects.filter(article_title__icontains=q).values_list('article_title', 'article_slug'))
    articles_results = [{'title': title, 'content_type': 'article', 'dir': 'ltr', 'href' : reverse('article', kwargs={'article_slug' : slug})} for title, slug in articles]

    courses = list(Course.objects.filter(course_name__icontains=q).values_list('course_name', 'course_slug'))
    courses_results = [{'title': title, 'content_type': 'course', 'dir': 'ltr', 'href' : reverse('course', kwargs={'course_slug' : slug})} for title, slug in courses]

    combined_results = articles_results + courses_results

    return JsonResponse(combined_results, safe=False)
