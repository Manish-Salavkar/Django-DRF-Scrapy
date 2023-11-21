from typing import Any
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))

    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))

    username = forms.CharField(required=True, max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))

    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))

    company_name = forms.CharField(required=False, label='Company Name', widget=forms.TextInput(attrs={'class': 'company_name', 'placeholder': 'Enter Company Name'}))

    profile_type = forms.ChoiceField(choices=CustomUser.PROFILE_CHOICES, required=True, label='Profile Type')

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=True,
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_type', 'company_name']





class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture', 'resume', 'company_name', 'company_website', 'linkedin_profile', 'skills', 'education', 'experience', 'location']
        

class PasswordVerificationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'passwordInput'}))


class AccountDeletionForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        label='I understand that this action cannot be undone'
    )
    password = forms.CharField(
        required=True,
        label='confirm your password',
        widget=forms.PasswordInput
    )

class CreateJobForm(forms.Form):
    JOB_TYPES = [
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('intern', 'Intern'),
        ('temporary', 'Temporary'),
        ('contract', 'Contract'),
    ]
    SALARY_CHOICES = [
        ('range', 'Range'),
        ('starting_at', 'Starting At'),
        ('upto', 'Up To'),
        ('exact_rate', 'Exact Rate'),
    ]
    SALARY_UNITS = [
        ('month', 'Month'),
        ('year', 'Year'),
    ]

    job_title = forms.CharField(label='Job Title', widget=forms.TextInput(attrs={'class': 'form-control'}),)
    location = forms.CharField(label='Location', widget=forms.TextInput(attrs={'class': 'form-control'}),)
    job_type = forms.ChoiceField(label='Job Type', choices=JOB_TYPES, widget=forms.Select(attrs={'class': 'form-control'}),)
    salary_type = forms.ChoiceField(label='Salary Type', choices=SALARY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),)
    min_salary = forms.DecimalField(label='Min Salary', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}),)
    max_salary = forms.DecimalField(label='Max Salary', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}),)
    salary_unit = forms.ChoiceField(label='Salary Unit', choices=SALARY_UNITS, widget=forms.Select(attrs={'class': 'form-control'}),)
    job_description = forms.CharField(widget=CKEditorWidget(attrs={'id':'ckeditorwidgetid'}), label='Job Description')
