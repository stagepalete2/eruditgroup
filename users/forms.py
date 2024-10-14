from django.forms import forms, ModelForm, EmailField
from crispy_forms.layout import Submit, Layout
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


from .models import User

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Войти'))
        
class SignUpForm(UserCreationForm):
    email = EmailField(max_length=200, required=False)
    usable_password = None
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'lastname', 'phone', 'date_of_birth']