from django.urls import path
from vacancy.views import index, add_vacancy

app_name = 'vacancy'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_vacancy, name='add')
]
