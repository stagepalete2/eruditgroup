from django.urls import path

from .views import TeacherPage

urlpatterns = [
    path('<slug:slug>/', TeacherPage.as_view(), name='teacher'),
]