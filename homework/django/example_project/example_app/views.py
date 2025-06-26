from django.shortcuts import render
from example_app.models import Item
# Create your views here.


def index(request):
    example_item = Item.objects.get(id=1)
    return render(request, 'index.html',
                  context={'item': example_item})

