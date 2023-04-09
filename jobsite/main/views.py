from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from . forms import UserForm, Job_postingsForm, LoginForm, SearchForm
from . models import Users, Categories, Job_postings
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,  login, logout
# Create your views here.

def index(request):
    form = SearchForm()
    categories = Categories.objects.all()
    jobs_list = Job_postings.objects.all().order_by("id")

    # ------------------------------
    page = request.GET.get('page', 1)

    paginator = Paginator(jobs_list, 4)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    # -------------------------------

    return render(request, "main/index.html", {"categories":categories,
                                               "jobs":jobs,
                                               "form":form})

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def jop_posting(request):
    
    if request.method == "POST":
        form = Job_postingsForm(request.POST,  request.FILES)

        if form.is_valid():
    
            form_saving = form.save(commit=False)
            form_saving.user = request.user
            form.save()
            print("SAVED")
            messages.success(request, 'Job posted successfully! Thank you')
            return render(request, "main/post-jobs.html" , {"form":Job_postingsForm()})

        else:
            return render(request, "main/post-jobs.html" , {"form":form})
        
    else:
        form = Job_postingsForm()

    return render(request, "main/post-jobs.html", {"form":form})

def signup_type(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST,  request.FILES)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.success(request, 'Something went wrong')
                return render(request, "main/signup_type.html" , {"form":form})
                

        else:
            return render(request, "main/signup_type.html" , {"form":form})
        
    else:
        form = LoginForm()
    return render(request, "main/signup_type.html", {"form":form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def create_account(request, signUpType="None"):
    if signUpType == "employer":
        temp = "main/create-account-employer.html"

    elif signUpType == "worker":
        temp = "main/create-account.html"
        
    if request.method == "POST":
        form = UserForm(request.POST,  request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data["username"]
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_number']
            cv = request.FILES.get('cv', None)
            cover_letter = request.FILES.get('cover_letter', None)
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            is_employer = request.POST["is_employer"]
            print(is_employer)

            saving = User.objects.create_user(first_name=name, email=email, username=username, password=password)
            if saving:
                saving_users_model = Users(user = saving, phone = phone, cv = cv,
                                           cover_letter = cover_letter, 
                                           created_at = datetime.now(),
                                           is_employer=is_employer)
                saving_users_model.save()
            print("SAVED")
            messages.success(request, 'Account created successfully! Enjoy')
            return HttpResponseRedirect('/')

        else:
            return render(request, temp , {"form":form})
        
    else:
        form = UserForm()
    
    return render(request, temp , {"form":form})



def searching(request):
  
        
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['search_term']
            results_list = Job_postings.objects.filter(title__icontains = name)
            # ------------------------------
            page = request.GET.get('page', 1)

            paginator = Paginator(results_list, 4)
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)

            # -------------------------------
            print(results)

            return render(request, "main/job-list.html" , {"form":form, "results":results, "name":name})

        else:
            return render(request, "main/job-list.html" , {"form":form})
        
    else:
        form = SearchForm()
    
    return render(request, "main/job-list.html" , {"form":form})