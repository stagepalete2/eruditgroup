from django.forms import forms, ModelForm
from crispy_forms.layout import Submit, Layout
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import AuthenticationForm

from .models import User

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Войти'))