from django.urls import path
from estate.views import index


urlpatterns = [
    path('', index)
]
