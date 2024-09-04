from django.urls import path
from .views import HomePage, CatalogPage, CoursePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('courses/',  CatalogPage.as_view(), name='catalog'),
    path('courses/<int:pk>/', CoursePage.as_view(), name='course'),
]
