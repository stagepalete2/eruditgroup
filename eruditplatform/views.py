from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator

# Create your views here.
from .models import News, HotLink, GroupCourse

class PlatformHome(ListView):
    template_name = 'platform_news.html'
    model = News
    context_object_name = 'news'
    paginate_by = 2
    paginator = Paginator(News, per_page=2)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            url = list(filter(None, [part for part in reverse('platform_home').split('/') if part])),
        )
        return context
    
    
class PlatformNewsDetail(DetailView):
    template_name = 'platform_news_detail.html'
    model = News
    context_object_name = 'new'
    slug_field = 'news_slug' 
    slug_url_kwarg = 'news_slug'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(self.request.resolver_match.kwargs)
        context.update(
            test = reverse('platform_news', kwargs={'news_slug' : self.slug_field}),
            url = list(filter(None, [part for part in reverse('platform_news', kwargs={'news_slug' : self.request.resolver_match.kwargs['news_slug']}).split('/') if part])),
            news = News.objects.all()
        )
        return context
    
class PlatformDashboard(TemplateView):
    template_name = 'platform_dashboard.html'

    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            url = list(filter(None, [part for part in reverse('platform_dashboard').split('/') if part])),
            hot_links = HotLink.objects.all(),
        )
        return context
    
class PlatformCalendar(TemplateView):
    template_name = 'platform_calendar.html'
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            url = list(filter(None, [part for part in reverse('platform_calendar').split('/') if part])),
        )
        return context
    
class PlatformCourseDetail(DetailView):
    template_name = 'platform_course.html'
    model = GroupCourse
    context_object_name = 'Course'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'url': list(filter(None, [part for part in reverse('platform_course', kwargs={'pk' : self.object.pk}).split('/') if part]))
        })
        return context

# class PlatformCourseDetail(TemplateView):
#     template_name = 'platform_course.html'

#     # slug_url_kwarg = 'course_slug'
#     # slug_field = 'course_slug'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'url': list(filter(None, [part for part in reverse('platform_course').split('/') if part]))
#         })
#         return context
    
class PlatformCourseDetailGrades(TemplateView):
    template_name = 'platform_course_grade.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            url = list(filter(None, [part for part in reverse('platform_course_grades').split('/') if part]))
        )
        return context
class PlatformCourseAssignment(TemplateView):
    template_name = 'platform_assignment.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            url = list(filter(None, [part for part in reverse('platform_assignment').split('/') if part]))
        )
        return context
class PlatformCourseTest(TemplateView):
    template_name = 'platform_test.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            url = list(filter(None, [part for part in reverse('platform_course_test').split('/') if part]))
        )
        return context