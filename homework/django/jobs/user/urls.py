from django.urls import path
from user.views import users


urlpatterns = [
    path('', users, name='users')
]
