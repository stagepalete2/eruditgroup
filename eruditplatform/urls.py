from django.urls import path

from .views import PlatformHome, PlatformDashboard, PlatformCalendar, PlatformCourseDetail, PlatformCourseDetailGrades, PlatformCourseAssignment, PlatformCourseTest, PlatformNewsDetail

urlpatterns = [
    path('', PlatformHome.as_view(), name='platform_home'),
    path('news/<slug:news_slug>/', PlatformNewsDetail.as_view(), name='platform_news'),
    path('dashboard/', PlatformDashboard.as_view(), name='platform_dashboard'),
    path('calendar/', PlatformCalendar.as_view(), name='platform_calendar'),
    path('course/<int:pk>/', PlatformCourseDetail.as_view(), name='platform_course'),
    
    path('course/grade/', PlatformCourseDetailGrades.as_view(), name='platform_course_grades'),
    path('course/assignment/', PlatformCourseAssignment.as_view(), name='platform_assignment'),
    path('course/test/', PlatformCourseTest.as_view(), name='platform_course_test'),
]
