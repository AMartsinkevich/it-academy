from django.urls import path
from resume.views import resumes


urlpatterns = [
    path('', resumes, name='resumes')
]
