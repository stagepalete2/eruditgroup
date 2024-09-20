from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PlatformHome(TemplateView):
    template_name = 'news.html'
    
class PlatformDashboard(TemplateView):
    template_name = 'dashboard.html'
    
    
class PlatformCalendar(TemplateView):
    template_name = 'calendar.html'
    
class PlatformCourseDetail(TemplateView):
    template_name = 'platform_course.html'
    
class PlatformCourseDetailGrades(TemplateView):
    template_name = 'platform_course_grade.html'
    
class PlatformCourseAssignment(TemplateView):
    template_name = 'platform_assignment.html'
    
class PlatformCourseTest(TemplateView):
    template_name = 'platform_test.html'