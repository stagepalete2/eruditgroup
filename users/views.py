from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .models import User
from .forms import SignInForm
# Create your views here.

class SignInPage(LoginView):
    template_name = 'auth/signin.html'
    
    redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context.update(
            {
                'LoginForm' : self.form_class
            }
        )
        
        return context

    
class SignUpPage(CreateView):
    template_name = 'auth/signup.html'
    
class LogOutPage(LogoutView):
    ...
    
class Profile(DetailView):
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