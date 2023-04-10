from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    cv = models.FileField(upload_to="Resumes/", null=True, blank=True)
    cover_letter = models.FileField(upload_to="CoverLetters/", null=True, blank=True)
    is_employer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

class  Categories(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    icon = models.ImageField(upload_to="Categories/", blank=True, null=True)
    icon_class = models.CharField(max_length=600, null=True, blank=True, help_text='get these at https://fontawesome.com/ version/5.10.0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Job_postings(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    howtoapply = models.TextField(null=True, blank=True)
    is_fulltime = models.BooleanField(default=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    company_logo = models.ImageField(upload_to="companyLogos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline =  models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


job_applications_status = (
    ("pending", "pending"),
    ("reviewed", "reviewed"),
    ("hired", "hired"),
    ("rejected", "rejected")
)
class Job_applications(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job_posting_id = models.ForeignKey(Job_postings, null=True, blank=True, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="Resumes/", null=True, blank=True)
    cover_letter = models.FileField(upload_to="CoverLetters/", null=True, blank=True)
    status = models.CharField(max_length=100, blank=True, null=True, choices=job_applications_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.job_posting_id



    