from django.urls import path
from example_app.views import index


urlpatterns = [
    path('', index)
]
