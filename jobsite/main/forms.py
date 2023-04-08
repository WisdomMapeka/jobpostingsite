from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, DateInput
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . models import Job_postings
from django.utils.translation import gettext_lazy as _
import datetime

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your Name"}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your userName"}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your email"}))
    phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your phone"}))
    cv = forms.FileField(required=False, widget=forms.TextInput(attrs={'class': "form-control-file", "placeholder":"Your password", "type":"file"}))
    cover_letter = forms.FileField(required=False, widget=forms.TextInput(attrs={'class': "form-control-file", "placeholder":"Your password", "type":"file"}))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your password"}))
    repeat_password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Repeat password"}))
    # is_employer = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Repeat password"}))

    def clean_username(self): 
        username = self.cleaned_data["username"]
        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('User already Exists, Try another name')
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already Exists, Try another name')
            return email


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password  = cleaned_data.get("repeat_password")

        if password and repeat_password:
            if password != repeat_password:
                self.add_error('password', 'Passwords does not match, try again ')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your userName"}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your email"}))   
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your password"}))
    def clean_username(self): 
        username = self.cleaned_data["username"]
        if username:
            if User.objects.filter(username=username).exists():
                pass
            else:
                raise forms.ValidationError('User Does Not Exist, Signup To login')
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email:
            if User.objects.filter(email=email).exists():
                pass
            else:
                raise forms.ValidationError('Email Does Not Exist, Signup To login')
            return email



class Job_postingsForm(ModelForm):
    deadline = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': "form-control"}))

    class Meta:
        model = Job_postings
        exclude = ["user", "updated_at", "created_at"]
        widgets = {
            "category": Select(attrs={'class': "form-control", "type":"text"}),
            "title": TextInput(attrs={'class': "form-control",  "type":"text"}),
            "description": Textarea(attrs={'class': "form-control",  "type":"text"}),
            "howtoapply" : Textarea(attrs={'class': "form-control",  "type":"text"}),
            "is_fulltime": TextInput(attrs={'class': "form-check-input",  "type":"checkbox"}),
            "location": TextInput(attrs={'class': "form-control",  "type":"text"}),
            "salary": TextInput(attrs={'class': "form-control",  "type":"text"}),
            "company": TextInput(attrs={'class': "form-control",  "type":"text"}),
            "company_logo": TextInput(attrs={'class': "form-control-file",  "type":"file"}),
            # "deadline ": forms.widgets.DateInput(attrs={'type': 'date'})
        }


