from django.urls import path

from .views import PlatformHome, PlatformDashboard, PlatformCalendar, PlatformCourseDetail, PlatformCourseGrades, PlatformCourseAssignment, PlatformCourseTest, PlatformNewsDetail, PlatformCourseAttendacne

urlpatterns = [
    path('', PlatformHome.as_view(), name='platform_home'),
    path('news/<slug:news_slug>/', PlatformNewsDetail.as_view(), name='platform_news'),
    path('dashboard/', PlatformDashboard.as_view(), name='platform_dashboard'),
    path('calendar/', PlatformCalendar.as_view(), name='platform_calendar'),
    path('course/<int:pk>/', PlatformCourseDetail.as_view(), name='platform_course'),
    
    path('course/<int:pk>/grade/', PlatformCourseGrades.as_view(), name='platform_course_grades'),
    path('course/assignment/<int:pk>/', PlatformCourseAssignment.as_view(), name='platform_assignment'),
    path('course/test/<int:pk>/', PlatformCourseTest.as_view(), name='platform_course_test'),
    path('course/<int:pk>/attendance/', PlatformCourseAttendacne.as_view(), name='platoform_course_attendance')
]
