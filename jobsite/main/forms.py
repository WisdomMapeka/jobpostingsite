from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your Name"}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your userName"}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your email"}))
    phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your phone"}))
    cv = forms.FileField(required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your password", "type":"file"}))
    cover_letter = forms.FileField(required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your password", "type":"file"}))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your password"}))
    repeat_password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Repeat password"}))
    is_employer = forms.BooleanField()

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