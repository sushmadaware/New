from django import forms
from .models import StudentModel

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
