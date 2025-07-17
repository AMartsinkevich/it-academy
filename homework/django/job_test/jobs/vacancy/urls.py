from django.urls import path
from vacancy.views import index, add, remove, show

app_name = 'vacancy'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('remove/', remove, name='remove'),
    path('show/', show, name='show'),
]
