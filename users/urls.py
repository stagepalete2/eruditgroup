from django.urls import path

from .views import SignInPage, SignUpPage, LogOutPage, Profile

urlpatterns = [
    path('signin/', SignInPage.as_view(), name='signin'),
    path('signup/', SignUpPage.as_view(), name='signup'),
    path('logout/', LogOutPage.as_view(), name='logout'),
    path('<int:pk>/', Profile.as_view(), name='profile'),
]
