from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("postjob/", views.jop_posting, name="job_posting"),
    path('createaccount/<str:signUpType>/', views.create_account, name="create_account"),
    path('signup-type/', views.signup_type, name="signup_type"),
]