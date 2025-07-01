from django.urls import path
from vacancy.views import vacancies


urlpatterns = [
    path('', vacancies, name='vacancies')
]
