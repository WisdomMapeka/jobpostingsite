from django.contrib import admin
from . models import User, Users, Categories, Job_postings

# Register your models here.
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Job_postings)
