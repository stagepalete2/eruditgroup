from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator

# Create your views here.
from .models import News, HotLink, GroupCourse, CourseAssignment, AssignmentGrade, CourseLesson

class PlatformHome(ListView):
    template_name = 'platform_news.html'
    model = News
    context_object_name = 'news'
    paginate_by = 2
    paginator = Paginator(News, per_page=2)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        groupcourses = GroupCourse.objects.filter(group__group_participants=self.request.user)
        
        context.update(
            url = list(filter(None, [part for part in reverse('platform_home').split('/') if part])),
            courses = groupcourses
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
    
class PlatformDashboard(ListView):
    template_name = 'platform_dashboard.html'
    model = GroupCourse
    context_object_name = 'courses'
    
    def get_deadlines(self):
        ...
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        courses = self.model.objects.filter(group__group_participants=self.request.user)

        deadlines = CourseAssignment.objects.filter(
            assignment_lesson__groupcourse__in=courses
        ).order_by('-assignment_due')

            
        context.update(
            url = list(filter(None, [part for part in reverse('platform_dashboard').split('/') if part])),
            hot_links = HotLink.objects.all(),
            deadlines = deadlines
        )
        return context
    
class PlatformCalendar(ListView):
    template_name = 'platform_calendar.html'
    model = GroupCourse
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        groups = GroupCourse.objects.filter(group__group_participants=self.request.user)
        
        schedule = {}
        
        for group in groups:
            for timetable in group.time_table.all():
                schedule[timetable.days_of_the_week] = {timetable.hours_of_the_week.__str__()[0:5] : group.course.course_name}
        
    
        print(schedule)
        
        context.update(
            url = list(filter(None, [part for part in reverse('platform_calendar').split('/') if part])),
            schedule = schedule,
            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']     
        )
        return context
    
class PlatformCourseDetail(DetailView):
    template_name = 'platform_course.html'
    model = GroupCourse
    context_object_name = 'Course'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignments = []
        assignments.extend(CourseAssignment.objects.filter(assignment_lesson__in=self.object.group_lesson.all()))
        context.update(
            url = list(filter(None, [part for part in reverse('platform_course', kwargs={'pk' : self.object.pk}).split('/') if part])),
            assignments = assignments
        )
        return context

    
class PlatformCourseGrades(DetailView):
    template_name = 'platform_course_grade.html'
    model = GroupCourse
    context_object_name = 'Grades'
    
    def calculate_course_total(self, assignments):
        course_total = {'grade': 0, 'range': 0, 'percentage': 0}
        
        for assignment in assignments:
            course_total['grade'] += assignment.grade
            course_total['range'] += assignment.grade_max

        if course_total['range'] > 0:
            course_total['percentage'] = (course_total['grade'] / course_total['range']) * 100
        else:
            course_total['percentage'] = 0

        return course_total['percentage']

    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        group_course = GroupCourse.objects.filter(group__group_participants=self.request.user, id=self.object.pk).first()
        group_lessons = group_course.group_lesson.all()
        
        course_assignment = CourseAssignment.objects.filter(assignment_lesson__in=group_lessons).first()
        assignments_grades = AssignmentGrade.objects.filter(student=self.request.user, assignment=course_assignment)
        
        context.update(
            url = list(filter(None, [part for part in reverse('platform_course_grades', kwargs={'pk' : self.object.pk}).split('/') if part])),
            assignments = assignments_grades,
            course_total = self.calculate_course_total(assignments_grades),
        )
        return context
    
class PlatformCourseAssignment(DetailView):
    template_name = 'platform_assignment.html'
    model = CourseAssignment
    context_object_name = 'assignment'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        
        context.update(
            url = list(filter(None, [part for part in reverse('platform_assignment', kwargs={'pk' : self.object.pk}).split('/') if part])),
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
    
    
class PlatformCourseAttendacne(DetailView):
    template_name = 'platform_attendance.html'
    model = GroupCourse
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        coursegroup = GroupCourse.objects.filter(group__group_participants=self.request.user, course=self.object.pk).first()
        lessons = coursegroup.group_lesson.all()
        
        
                
        context.update(
            url = list(filter(None, [part for part in reverse('platoform_course_attendance', kwargs={'pk' : self.object.pk}).split('/') if part])),
            lessons = lessons
        )   
        
        return context
    