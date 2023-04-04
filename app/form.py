from django import forms
from .models import *

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.TextInput(attrs={'class':"form-control"}),
            'password':forms.PasswordInput(attrs={'class':"form-control"})
        }