from django.urls import path

from .views import get_free_teachers

urlpatterns = [
    path('get_free_teachers/', get_free_teachers, name='api-get_free_teachers'),
    
]
