from django.urls import path
from .views import HomePage, CatalogPage, CoursePage, ScheduleConstructor

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('courses/',  CatalogPage.as_view(), name='catalog'),
    path('courses/<slug:course_slug>/', CoursePage.as_view(), name='course'),
    path('courses/schedule_constructor/1/', ScheduleConstructor.as_view(), name='schedule_contructor')
]
