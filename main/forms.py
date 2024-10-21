from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'email', 'roll_number', 'department', 'year_of_study',
            'resume', 'skills', 'degree', 'institution',
            'year_of_graduation', 'phone_number'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your roll number'}),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your department'}),
            'year_of_study': forms.Select(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-group checkbox-group'}),
            'degree': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your degree'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your institution'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            
        }
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [ 'linkedin', 'portfolio', 'resume','cover_letter']
        widgets = {
            'interview_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'linkedin': forms.URLInput(attrs={
                'placeholder': 'Enter your LinkedIn profile URL',
                'class': 'form-control'
            }),
            'portfolio': forms.URLInput(attrs={
                'placeholder': 'Enter your Portfolio URL',
                'class': 'form-control'
            }),
             
        }  
               