from django.contrib import admin

# Register your models here.
from .models import News, HotLink, Groups, GroupCourse, TimeTable, GroupAttendance, AssignmentGrade, AssignmentAttachments, CourseAssignment, CourseLesson, AssignmentSubmissions, AssignmentSubmissionFiles

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'published',
    ]
    prepopulated_fields = {'news_slug' : ['title']}


@admin.register(HotLink)
class HotLinkAdmin(admin.ModelAdmin):
    list_display = [
        'new',
    ]
    
@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
    ]
    
@admin.register(GroupCourse)
class GroupCourseAdmin(admin.ModelAdmin):
    list_display = [
        'course',
        'group',
        'teacher',
    ]


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = [
        'days_of_the_week',
        'hours_of_the_week'
    ]


@admin.register(GroupAttendance)
class GroupAttendanceAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'date',
        'status',
        'remark'
    ]

@admin.register(AssignmentGrade)
class AssignmentGradeAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'assignment',
        'grade',
        'grade_max',
        'feedback',
    ]

@admin.register(AssignmentAttachments)
class AssignmentAttachmentsAdmin(admin.ModelAdmin):
    list_display = [
        'file'
    ]

@admin.register(CourseAssignment)
class CourseAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'assignment_name', 
        'assignment_opened',
        'assignment_due',
        'assignment_lesson',
        'created'
    ]
    
@admin.register(CourseLesson)
class CourseLessonAdmin(admin.ModelAdmin):
    list_display = [
        'lesson_title',
        'lesson_detail',
        'lesson_datetime',
    ]

@admin.register(AssignmentSubmissions)
class AssignmentSubmissionsAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'assignment',
        'created',
    ]

@admin.register(AssignmentSubmissionFiles)
class AssignmentSubmissionFilesAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'created'
    ]
    
