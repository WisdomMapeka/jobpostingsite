from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("postjob/", views.jop_posting, name="job_posting"),
    path('createaccount/<str:signUpType>/', views.create_account, name="create_account"),
    path('signup-type/', views.signup_type, name="signup_type"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('search/', views.searching, name='searching'),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about,  name="about")
]