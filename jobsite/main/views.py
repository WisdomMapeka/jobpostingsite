from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from . forms import UserForm
from . models import Users
from datetime import datetime
from django import forms
# Create your views here.

def index(request):
    return render(request, "main/index.html")

def jop_posting(request):
    return render(request, "main/post-jobs.html")

def signup_type(request):
    return render(request, "main/signup_type.html")

def create_account(request, signUpType="None"):
    if signUpType == "employer":
        temp = "main/create-account-employer.html"
        is_employer = True
    elif signUpType == "worker":
        temp = "main/create-account.html"
        is_employer = False

    print(signUpType)
    if request.method == "POST":
        form = UserForm(request.POST,  request.FILES)

        if form.is_valid():
            print(request.POST['name'])
            name = form.cleaned_data['name']
            username = form.cleaned_data["username"]
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_number']
            cv = request.FILES.get('cv', None)
            cover_letter = request.FILES.get('cover_letter', None)
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            saving = User.objects.create_user(first_name=name, email=email, username=username, password=password)
            if saving:
                saving_users_model = Users(user = saving, phone = phone, cv = cv,
                                           cover_letter = cover_letter, 
                                           created_at = datetime.now(),
                                           is_employer=is_employer)
                saving_users_model.save()
            print("SAVED")
            return HttpResponseRedirect('/')

        else:
            return render(request, temp , {"form":form})
        
    else:
        form = UserForm()
        # print(form.errors)
        # form = ContactUsForm(request.POST)
        # messages.add_message(request, messages.INFO, form.errors)
 
    # print(request.POST)
    # print(request.FILES)
    
    return render(request, temp , {"form":form})