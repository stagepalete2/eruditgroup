from collections import defaultdict
from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


# Create your views here.
from .models import AssignmentSubmissionFiles, News, HotLink, GroupCourse, CourseAssignment, AssignmentGrade, CourseLesson, AssignmentSubmissions, TimeTable
from .forms import SubmitAssignmentForm

class PlatformHome(LoginRequiredMixin, ListView):
    template_name = 'platform_news.html'
    model = News
    context_object_name = 'news'
    paginate_by = 2
    paginator = Paginator(News, per_page=2)
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context.update(
            url = list(filter(None, [part for part in reverse('platform_home').split('/') if part])),
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user)
        )
        return context
    
    
class PlatformNewsDetail(LoginRequiredMixin, DetailView):
    template_name = 'platform_news_detail.html'
    model = News
    context_object_name = 'new'
    slug_field = 'news_slug' 
    slug_url_kwarg = 'news_slug'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(self.request.resolver_match.kwargs)
        context.update(
            test = reverse('platform_news', kwargs={'news_slug' : self.slug_field}),
            url = list(filter(None, [part for part in reverse('platform_news', kwargs={'news_slug' : self.request.resolver_match.kwargs['news_slug']}).split('/') if part])),
            news = News.objects.all(),
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user)
        )
        return context
    
class PlatformDashboard(LoginRequiredMixin, ListView):
    template_name = 'platform_dashboard.html'
    model = GroupCourse
    context_object_name = 'courses'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_queryset(self):
        """
        Filter GroupCourse by logged-in user's participation in group_participants.
        """
        user = self.request.user
        return GroupCourse.objects.filter(group__group_participants=user)
    
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
            deadlines = deadlines,
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user)
        )
        return context
    
class PlatformCalendar(LoginRequiredMixin, ListView):
    template_name = 'platform_calendar.html'
    model = GroupCourse
    context_object_name = 'courses'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        hours_of_week = "09:00,10:00,11:00,12:00,13:00,14:00,15:00,16:00,17:00,18:00,19:00,20:00".split(",")
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        tim = TimeTable.objects.first()
        schedule = []
        for hour in hours_of_week:
            for day in days_of_week:
                schedule.append({'day' : day, 'hour' : hour, 'courses' : GroupCourse.objects.filter(group__group_participants=self.request.user, time_table__days_of_the_week = day, time_table__hours_of_the_week = hour[0:5])})
        context.update(
            schedules = schedule,
            days_of_week = days_of_week,
            hours_of_week = hours_of_week,
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user),
        )
        return context
    
class PlatformCourseDetail(LoginRequiredMixin, DetailView):
    template_name = 'platform_course.html'
    model = GroupCourse
    context_object_name = 'Course'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_queryset(self):
        """
        Filter GroupCourse by logged-in user's participation in group_participants.
        """
        user = self.request.user
        return GroupCourse.objects.filter(group__group_participants=user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignments = []
        assignments.extend(CourseAssignment.objects.filter(assignment_lesson__in=self.object.group_lesson.all()))
        
        timetables = self.get_object().time_table.all()
    
        # Preprocessing timetable data by days of the week
        timetable_by_day = defaultdict(list)
        
        # This will group all timetables by the day of the week
        for timetable in timetables:
            timetable_by_day[timetable.days_of_the_week].append(timetable.hours_of_the_week)
        
        
        context.update(
            assignments = assignments,
            timetable_by_day = timetable_by_day,
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user),
            
        )
        return context

    
class PlatformCourseGrades(LoginRequiredMixin, DetailView):
    template_name = 'platform_course_grade.html'
    model = GroupCourse
    context_object_name = 'Grades'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
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
        
        course_assignments = CourseAssignment.objects.filter(assignment_lesson__in=group_lessons)
        assignments_grades = AssignmentGrade.objects.filter(student=self.request.user, assignment__in=course_assignments)
        
        context.update(
            assignments = assignments_grades,
            course_total = self.calculate_course_total(assignments_grades),
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user),
            
        )
        return context
    
class PlatformCourseAssignment(LoginRequiredMixin, DetailView):
    template_name = 'platform_assignment.html'
    model = CourseAssignment
    context_object_name = 'assignment'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        fileForm = SubmitAssignmentForm(request.POST, request.FILES)
        
        student = self.request.user
        submission, created = AssignmentSubmissions.objects.get_or_create(
            student=student, assignment=self.get_object()
        )  
        files = self.request.FILES.getlist('files')

        if fileForm.is_valid():
            for file in files:
                file_instance = AssignmentSubmissionFiles.objects.create(file=file)
                submission.files.add(file_instance)

        else:
            print(fileForm.errors)

        return redirect(reverse('platform_assignment', kwargs={'pk': self.get_object().id}))

            
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            submission = AssignmentSubmissions.objects.filter(student=self.request.user, assignment=self.object.pk).first(),
            grade = AssignmentGrade.objects.filter(student=self.request.user, assignment=self.object.pk).first(),
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user),
        )
        return context
    
    
    
class SubmitAssignment(LoginRequiredMixin, CreateView):
    model = AssignmentSubmissionFiles
    template_name = 'platform_assignment.html'
    fields = ['file', ]
    
class PlatformCourseTest(LoginRequiredMixin, TemplateView):
    template_name = 'platform_test.html'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user),
        )
        return context
    
    
class PlatformCourseAttendance(LoginRequiredMixin, DetailView):
    template_name = 'platform_attendance.html'
    model = GroupCourse
    context_object_name = 'Course'
    login_url = reverse_lazy('signin')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        coursegroup = GroupCourse.objects.filter(group__group_participants=self.request.user, course=self.object.pk).first()
        lessons = coursegroup.group_lesson.all()
        
        
                
        context.update(
            lessons = lessons,
            courses = GroupCourse.objects.filter(group__group_participants=self.request.user)
        )   
        
        return context
    