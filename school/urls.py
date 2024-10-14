from django.urls import path
from .views import HomePage, CatalogPage, CoursePage, ScheduleConstructor, search_input

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('courses/',  CatalogPage.as_view(), name='catalog'),
    path('courses/<slug:course_slug>/', CoursePage.as_view(), name='course'),
    path('courses/<slug:course_slug>/schedule_constructor/', ScheduleConstructor.as_view(), name='schedule_contructor'),
    path('search/', search_input, name='search')
]
