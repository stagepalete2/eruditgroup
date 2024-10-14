from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import User
from .forms import SignInForm, SignUpForm

# Create your views here.


class SignInPage(LoginView):
    template_name = 'auth/signin.html'
    redirect_authenticated_user = False
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context.update(
            LoginForm = self.form_class
        )
        
        return context

    
class SignUpPage(CreateView):
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('signin')

    def get_success_url(self) -> str:
        success_url = super().get_success_url()
        success_url += f'?isFormValid={True}'
        return success_url

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        self.isFormValid = False
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SignUpForm = self.form_class
        )
        return context

    
class LogOutPage(LoginRequiredMixin, LogoutView):
    ...
    

class Profile(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    model = User
    slug_field = 'username' 
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context