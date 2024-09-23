from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from users.models import User

# Create your views here.
# class TeacherPage(DetailView):
#     template_name = 'teacher.html'
#     model = User
    

class TeacherPage(TemplateView):
    template_name = 'teacher.html'
    # model = User
