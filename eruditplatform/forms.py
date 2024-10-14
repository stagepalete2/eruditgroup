from django.forms import forms
from .models import AssignmentSubmissionFiles

class SubmitAssignmentForm(forms.Form):
    class Meta:
        model = AssignmentSubmissionFiles
        fields = ['file',]