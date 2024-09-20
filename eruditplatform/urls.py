from django.urls import path

from .views import PlatformHome, PlatformDashboard, PlatformCalendar, PlatformCourseDetail, PlatformCourseDetailGrades, PlatformCourseAssignment, PlatformCourseTest

urlpatterns = [
    path('', PlatformHome.as_view(), name='home'),
    path('dashboard/', PlatformDashboard.as_view(), name='dashboard'),
    path('calendar/', PlatformCalendar.as_view(), name='calendar'),
    path('course/', PlatformCourseDetail.as_view(), name='course'),
    path('course/grade/', PlatformCourseDetailGrades.as_view(), name='course_grades'),
    path('course/assignment/', PlatformCourseAssignment.as_view(), name='assignment'),
    path('course/test/', PlatformCourseTest.as_view(), name='course_test'),
]
